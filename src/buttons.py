from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from .variables import MEDIUM_FONT_SIZE
from .tools.utils import isNumOrDot, isValidNumber
import math

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .display import Display
    from .info import Info
    from .main_window import MainWindow

class ButtonNumber(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        
        # btn name
        self.setObjectName('btn-number')

class ButtonText(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')

        # btn name
        self.setObjectName('btn-text')

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['🤔', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._calculation = None
        self._calculation_initial = 'calculation'
        self._calculation_left = None
        self._calculation_right = None
        self._calculation_op = None
        self._makeGridMask()
    
    # getters and setters
    @property
    def calculation(self):
        return self._calculation
    
    @calculation.setter
    def calculation(self, value):
        self._calculation = value
        self.info.setText(value)

    # btn grid
    def _makeGridMask(self):
        for i, row in enumerate(self._grid_mask):
            for j, btn in enumerate(row):
                if not isNumOrDot(btn):
                    button = ButtonText(btn)
                    self.addWidget(button, i, j)
                    self._connectNotNumberBtnClicked(button)
                else:
                    button = ButtonNumber(btn)
                    self.addWidget(button, i, j)
                    slot = self._makeBtnSlot(self._sentBtnTextToDisplay, button)
                    self._connectBtnClicked(button, slot)
                
    # btn connection
    def _connectBtnClicked(self, btn: QPushButton, slot: Slot):
        btn.clicked.connect(slot)

    # operations
    def _connectNotNumberBtnClicked(self, btn: ButtonText):
        text = btn.text()

        if text == 'C':
            self._connectBtnClicked(btn, self._clear)

        elif text == '◀':
            self._connectBtnClicked(btn, self.display.backspace)

        elif text in '+-/*^':
            self._connectBtnClicked(
                btn,
                self._makeBtnSlot(self._operatorClicked, btn)
            )

        elif text == '=':
            self._connectBtnClicked(btn, self._eq)

    # btn slot
    def _makeBtnSlot(self, func, *args, **kwargs):
        @Slot()
        def _Slot():
            func(*args, **kwargs)
        return _Slot

    # info label text
    def _sentBtnTextToDisplay(self, button: QPushButton):
        btn_text = button.text()
        new_display_value = self.display.text() + btn_text
        if not isValidNumber(new_display_value):
            self._infoBox('Operação inválida!')
            return
        self.display.insert(btn_text)

    # display clear
    def _clear(self):
        self._calculation_left = None
        self._calculation_right = None
        self._calculation_op = None
        self.calculation = self._calculation_initial
        self.display.clear()

    # operation logic
    def _operatorClicked(self, button: ButtonText):
        btn_text = button.text()
        display_text = self.display.text()
        self.display.clear()

        if not isValidNumber(display_text) and self._calculation_left is None:
            self._infoBox('Operação inválida')
            return
        
        if self._calculation_left is None:
            self._calculation_left = float(display_text)

        self._calculation_op = btn_text
        self.calculation = f'{self._calculation_left} {self._calculation_op} ??'
    
    # result calculation
    def _eq(self):
        display_text = self.display.text()

        if not isValidNumber(display_text):
            self._infoBox('Operação inválida!')
            return  
        
        self._calculation_right = float(display_text)
        self.calculation = f'{self._calculation_left} {self._calculation_op} {self._calculation_right}'

        result = 'error'
        try:
            if '^' in self.calculation:
                result = math.pow(self._calculation_left, self._calculation_right)
            else:
                result = eval(self.calculation)
        except ZeroDivisionError:
            self._infoBox('Impossível dividir por zero!')
        except OverflowError:
            self._infoBox('Número muito grande!')
        
        self.display.clear()
        self.info.setText(f'{self.calculation} = {result}')
        self._calculation_left = result
        self._calculation_right = None

        if result == 'error':
            self._clear()

    # error boxes
    def _errorBox(self, msg):
        msg_box = self.window.makeMsgBox()
        msg_box.setText(msg)
        msg_box.setIcon(msg_box.Icon.Critical)

        # description
        msg_box.setInformativeText('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mihi, inquam, qui te id ipsum rogavi?')

        # btns
        msg_box.setStandardButtons(
            msg_box.StandardButton.Ok |
            msg_box.StandardButton.Cancel |
            msg_box.StandardButton.Close
        )
        msg_box.button(msg_box.StandardButton.Ok).setText('OK😎')
        msg_box.button(msg_box.StandardButton.Ok).setStyleSheet('font-size:20px; background-color: aqua;' 
                                                                'border-radius: 5px; padding: 5px;')
        
        msg_box.button(msg_box.StandardButton.Cancel).setText('Cancelar😉')
        msg_box.button(msg_box.StandardButton.Cancel).setStyleSheet('font-size:20px; background-color: aqua;' 
                                                                'border-radius: 5px; padding: 5px;')
        
        msg_box.button(msg_box.StandardButton.Close).setText('Fechar😁')
        msg_box.button(msg_box.StandardButton.Close).setStyleSheet('font-size:20px; background-color: aqua;' 
                                                                'border-radius: 5px; padding: 5px;')

        result = msg_box.exec()
        if result == msg_box.StandardButton.Ok:
            print('Ok')
        elif result == msg_box.StandardButton.Cancel:
            print('Cancel')
        elif result == msg_box.StandardButton.Close:
            print('Close')
    
    def _infoBox(self, msg):
        msg_box = self.window.makeMsgBox()
        msg_box.setText(msg)
        msg_box.setIcon(msg_box.Icon.Information)

        # btns
        msg_box.setStandardButtons(
            msg_box.StandardButton.Ok
        )
        msg_box.button(msg_box.StandardButton.Ok).setText('OK😎')
        msg_box.button(msg_box.StandardButton.Ok).setStyleSheet('font-size:20px; background-color: aqua;' 
                                                                'border-radius: 5px; padding: 5px;')
        
        msg_box.exec()
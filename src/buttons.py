from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from .variables import MEDIUM_FONT_SIZE
from .tools.utils import isNumOrDot, isValidNumber

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .display import Display
    from .info import Info

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
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs) -> None:
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
        self._calculation = None
        self._makeGridMask()
    
    # getters and setter
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
                if isNumOrDot(btn):
                    button = ButtonNumber(btn)
                else:
                    button = ButtonText(btn)

                button_slot = self.makeBtnSlot(self.sentBtnTextToDisplay, button)
                button.clicked.connect(button_slot)
                self.addWidget(button, i, j)

    # btn slot
    def makeBtnSlot(self, func, *args, **kwargs):
        @Slot()
        def _Slot():
            func(*args, **kwargs)
        return _Slot

    # info label text
    def sentBtnTextToDisplay(self, button: QPushButton):
        btn_text = button.text()
        new_display_value = self.display.text() + btn_text
        if not isValidNumber(new_display_value):
            return
        self.display.insert(btn_text)
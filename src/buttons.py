from PySide6.QtWidgets import QPushButton, QGridLayout
from .variables import MEDIUM_FONT_SIZE

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
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['🤔', '0', '.', '='],
        ]
        self._makeGridMask()
    
    def _makeGridMask(self):
        for i, row in enumerate(self._grid_mask):
            for j, btn in enumerate(row):
                if btn in '0123456789.':
                    button = ButtonText(btn)
                else:
                    button = ButtonNumber(btn)
                self.addWidget(button, i, j)
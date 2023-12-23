from PySide6.QtWidgets import QPushButton
from .variables import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from .variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUN_WIDTH

class Display(QLineEdit):
    # my signals
    eq_signal = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        margin = [TEXT_MARGIN for _ in range(4)]
        self.setTextMargins(*margin)

        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setPlaceholderText('Sua calculadora')

    # events and signals
    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return]

        if is_enter:
            self.eq_signal.emit()
            # disable specific key
            return event.ignore()

        # disables all keys (return super OFF)
        # return super().keyPressEvent(event)
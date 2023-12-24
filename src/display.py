from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from .variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUN_WIDTH
from .tools.utils import isEmpty, isNumOrDot

class Display(QLineEdit):
    # my signals
    eq_signal = Signal()
    delete_signal = Signal()
    esc_signal = Signal()
    num_or_dot_signal = Signal(str)

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
        key_text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        is_delete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_esc = key in [KEYS.Key_Escape, KEYS.Key_C]

        if is_enter:
            self.eq_signal.emit()
            # disable specific key
            return event.ignore()

        if is_delete:
            self.delete_signal.emit()
            # disable specific key
            return event.ignore()

        if is_esc:
            self.esc_signal.emit()
            # disable specific key
            return event.ignore()

        if isEmpty(key_text):
            return event.ignore()

        if isNumOrDot(key_text):
            self.num_or_dot_signal.emit(key_text)
            print(key_text)

        # disables all keys (return super OFF)
        # return super().keyPressEvent(event)
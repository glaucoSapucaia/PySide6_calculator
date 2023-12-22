from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon
from .variables import ICON
from .display import Display
from .info import Info

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # window title
        self.setWindowTitle('Sapucaia Calculator')

        # window icon
        icon = QIcon(str(ICON))
        self.setWindowIcon(icon)

        # definitions
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.info = Info()
        self.display = Display()

        # relations
        self.setCentralWidget(self.cw)
        self.cw.setLayout(self.v_layout)

    # add widgets
    def addWidgetToVLayout(self, widget: QWidget) -> None:
        self.v_layout.addWidget(widget)

    # window size
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
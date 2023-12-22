from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # window title
        self.setWindowTitle('Sapucaia Calculator')

        # definitions
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()

        # relations
        self.setCentralWidget(self.cw)
        self.cw.setLayout(self.v_layout)

    # window size
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
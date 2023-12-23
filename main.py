from PySide6.QtWidgets import QApplication
from src import MainWindow
from src.variables import QSS_STYLE
import sys

if __name__ == '__main__':
    # definitions
    app = QApplication(sys.argv)
    window = MainWindow()

    # QSS style
    with open(str(QSS_STYLE), 'r') as file:
        _style = file.read()
        app.setStyleSheet(_style)

    # relations
    window.addWidgetToVLayout(window.info)
    window.addWidgetToVLayout(window.display)

    # executions
    window.adjustFixedSize()
    window.show()
    app.exec()
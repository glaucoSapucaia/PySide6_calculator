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
    window.addWidgetToVLayout(window.btn1)
    window.addWidgetToVLayout(window.btn2)
    window.addWidgetToVLayout(window.btn3)
    window.addWidgetToVLayout(window.btn4)

    # executions
    window.adjustFixedSize()
    window.show()
    app.exec()
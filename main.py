from PySide6.QtWidgets import QApplication
from src import MainWindow
import sys

if __name__ == '__main__':
    # definitions
    app = QApplication(sys.argv)
    window = MainWindow()

    # relations
    window.addWidgetToVLayout(window.info)
    window.addWidgetToVLayout(window.display)

    # executions
    window.adjustFixedSize()
    window.show()
    app.exec()
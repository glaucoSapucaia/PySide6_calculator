from PySide6.QtWidgets import QApplication, QLabel
from src import MainWindow
import sys

if __name__ == '__main__':
    # definitions
    app = QApplication(sys.argv)
    window = MainWindow()

    # labels
    label1 = QLabel('My Label')
    label1.setStyleSheet('font-size: 100px; background-color: black; color: white;')

    # relations
    window.addWidgetToVLayout(label1)

    # executions
    window.adjustFixedSize()
    window.show()
    app.exec()
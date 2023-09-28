import sys
from PyQt6.QtWidgets import QApplication

from widgets.view.mainView import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainView()
    window.show()
    app.exec()

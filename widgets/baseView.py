from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget


class BaseView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_background(self, color):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(color))
        self.setPalette(p)

    def update_proc(self):
        pass

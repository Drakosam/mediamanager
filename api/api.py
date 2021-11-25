from PySide6.QtCore import *
from PySide6.QtCore import QObject


class Api(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    @Slot()
    def test(self):
        print('xxx')
        return 'xxx'
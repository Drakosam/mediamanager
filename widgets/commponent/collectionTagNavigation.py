from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QPushButton

from collection import collection_manager
from enums.enentNames import EventName
from utyllity import observer
from widgets.shered.baseView import BaseView


class CollectionTagNavigation(BaseView):
    def __init__(self, parent: BaseView = None):
        super().__init__(parent)
        self.set_background('#660000')
        self._setup_button()
        self._parent = parent

    def _setup_button(self):
        self.update_tag = QPushButton(self)

        self.update_tag.setText('Update Tag')
        self.update_tag.clicked.connect(self._update_collection)

    @staticmethod
    def _update_collection():
        print('update')

    def resizeEvent(self, a0) -> None:
        super().resizeEvent(a0)

        butt_width = 100

        self.update_tag.resize(butt_width, self.size().height())
        self.update_tag.move(butt_width * 0, 0)


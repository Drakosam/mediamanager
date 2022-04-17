from PyQt6.QtWidgets import QListWidget

from collection import collection_manager
from widgets.baseView import BaseView


class CollectionView(BaseView):
    def __init__(self, parent: BaseView = None):
        super().__init__(parent)
        self.set_background('#fff')
        self.c_list = QListWidget(self)
        self.c_list.clicked.connect(self._update_selected_item)
        self._update_list()
        self._parent: BaseView = parent

    def _update_selected_item(self):
        collection_manager.set_collection_by_name(self.c_list.currentItem().text())
        self._parent.update_proc()

    def _update_list(self):
        self.c_list.clear()
        for i in collection_manager.get_collection_names():
            self.c_list.addItem(i)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.c_list.resize(self.size())

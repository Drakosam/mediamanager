from PyQt6.QtWidgets import QListWidget

from collection import collection_manager
from enums.enentNames import EventName
from utyllity import observer
from widgets.baseView import BaseView


class CollectionListView(BaseView):
    def __init__(self, parent: BaseView = None):
        super().__init__(parent)
        self.set_background('#fff')
        self.c_list = QListWidget(self)
        self.c_list.clicked.connect(self._update_selected_item)
        self._parent: BaseView = parent
        observer.register_event(EventName.NEW_IMAGE, self._update_list)

    def _update_selected_item(self):
        collection_manager.set_collection_by_name(self.c_list.currentItem().text())
        observer.call_event(EventName.NEW_IMAGE)

    def _update_list(self):
        self.c_list.clear()
        for i in collection_manager.get_collection_names():
            self.c_list.addItem(i)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.c_list.resize(self.size())

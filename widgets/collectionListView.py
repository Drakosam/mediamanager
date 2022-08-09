
from collection import collection_manager
from enums.enentNames import EventName
from utyllity import observer
from widgets.baseView import BaseView
from widgets.customListWidged import CustomListWidget


class CollectionListView(BaseView):
    def __init__(self, parent: BaseView = None):
        super().__init__(parent)
        self.set_background('#fff')
        self.c_list = CustomListWidget(self)
        self._parent: BaseView = parent
        observer.register_event(EventName.NEW_COLLECTION, self._update_list)

    def _update_list(self):
        self.c_list.clear()
        for i in collection_manager.get_collection_names():
            self.c_list.add_item(i)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.c_list.resize(self.size())

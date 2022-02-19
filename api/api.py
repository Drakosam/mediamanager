import json

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtCore import QObject


class Api(QObject):
    collectionListChanged = QtCore.Signal()
    collection_list = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.collection_list.append({'name': 'xxx-xxx-xxx', 'index': 0})
        self.collection_list.append({'name': 'aaa-aaa-aaa', 'index': 1})
        self.collection_list.append({'name': 'ddd-ddd-ddd', 'index': 2})
        self.collection_list.append({'name': 'hhh-hhh-hhh', 'index': 3})

    def run_init_view(self):
        self.collectionListChanged.emit()

    @Slot()
    def test(self):
        print('xxx')
        return 'xxx'

    @Slot(int)
    def pickCollection(self, no_data):
        print(no_data)
        return 'xxx'

    def collection_list_set(self, new_collection_list):
        self.collection_list = new_collection_list

    def collection_list_get(self):
        return json.dumps(self.collection_list)

    collectionList = QtCore.Property(
        str,
        fset=collection_list_set,
        fget=collection_list_get,
        notify=collectionListChanged
    )

# class CollectionItem(QtCore.QObject):
#     COLUMNS = ('name','index',)
#     def __init__(self, name, index):
#         super(CollectionItem, self).__init__()
#         self._name = name
#         self._index = index
#         self.setRoleNames(dict(enumerate(CollectionItem.COLUMNS)))

from PyQt6.QtWidgets import QMainWindow, QTabWidget

from widgets.collectionSetings import CollectionSettings
from widgets.mainCollectionView import MainCollectionView
from widgets.mainTagView import MainTagView


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.main_collection_view = MainCollectionView(self)
        self.main_tag_view = MainTagView(self)
        self.collection_settings = CollectionSettings(self)

        self.tabView = QTabWidget(self)
        self.tabView.addTab(self.main_collection_view, 'Image')
        self.tabView.addTab(self.main_tag_view, 'Tags')
        self.tabView.addTab(self.collection_settings, 'Settings')

        tab_pos = self.tabView.tabPosition()
        self.tabView.setTabPosition(tab_pos.West)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.tabView.resize(self.size())


from widgets.baseView import BaseView

from widgets.collectionListView import CollectionListView
from widgets.imageNavigationView import ImageNavigationView
from widgets.imageView import ImageView


class MainCollectionView(BaseView):
    def __init__(self, parent=BaseView):
        super().__init__(parent)
        self.image_view = ImageView(self)
        self.collection_list_view = CollectionListView(self)
        self.navigation_image_view = ImageNavigationView(self)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.image_view.resize(self.width() - 300, self.height() - 40)
        self.navigation_image_view.resize(self.width() - 300, 40)
        self.collection_list_view.resize(300, self.height())

        self.collection_list_view.move(self.width() - 300, 0)
        self.navigation_image_view.move(0, self.height() - 40)


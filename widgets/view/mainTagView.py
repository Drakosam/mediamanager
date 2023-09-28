from widgets.commponent.collectionTagNavigation import CollectionTagNavigation
from widgets.shered.baseView import BaseView

from widgets.commponent.collectionListView import CollectionListView
from widgets.commponent.imageNavigationView import ImageNavigationView
from widgets.commponent.imageView import ImageView



class MainTagView(BaseView):
    def __init__(self, parent=BaseView):
        super().__init__(parent)
        self.height_collection = 400
        self.image_view = ImageView(self)
        self.collection_list_view = CollectionListView(self)
        self.tag_navigation = CollectionTagNavigation(self)

        self.navigation_image_view = ImageNavigationView(self)
        self.navigation_image_view.set_simpe_view()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)

        self.image_view.resize(self.width() - self.height_collection, self.height() - 40*2)
        self.navigation_image_view.resize(self.width() - self.height_collection, 40)
        self.collection_list_view.resize(self.height_collection, self.height())
        self.tag_navigation.resize(self.width() - self.height_collection, 40)

        self.collection_list_view.move(self.width() - self.height_collection, 0)
        self.navigation_image_view.move(0, self.height() - 40)
        self.tag_navigation.move(0, self.height() - 80)



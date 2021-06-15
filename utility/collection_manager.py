from typing import List
from utility import collection
from utility.collection import Collection


class CollectionManager():
    def __init__(self) -> None:
        self.collections: List[Collection] = []
        self.image_index = 0
        self.collection_index = 0
        self.show_collection: List[Collection] = []
        self.filter_tags: List[str] = []

    def next_image():
        pass
    
    def next_collection():
        pass

    def size(self):
        return len(self.collections)

    def add_collection(self, name = '', path = '', images: List[str] = [], collection:Collection = None )-> bool:
        
        if collection is not None and collection.valid():
            self.collections.append(collection)
            return True
        elif collection is not None:
            return False

        if not path or len(images) == 0 :
            return False
        
        if not name:
            path = name

        self.collections.append(Collection(name,path,images))

        return True

    def get_image(self , collection_index=-1, image_index=-1):
        if len(self.collections) == 0 or not collection_index < len(self.collections):
            return ''

        if collection_index > -1:
            self.collection_index = collection_index

        if image_index > -1:
            self.image_index = image_index

        return self.collections[self.collection_index].get_image(self.image_index)

    def get_collection_names()->List[str]:
        pass

    def toggle_tag_filter():
        pass
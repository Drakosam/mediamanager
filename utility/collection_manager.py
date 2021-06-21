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

    def next_image(self, step=1):
        self.image_index += step
        if self.image_index >= self.show_collection[self.collection_index].size():
            self.image_index = 0
        elif self.image_index < 0:
            self.image_index = self.show_collection[self.collection_index].size() - 1
    
    def next_collection(self, step=1):
        self.collection_index += step
        if self.collection_index >= len(self.show_collection):
            self.collection_index = 0
        elif self.collection_index < 0:
            self.collection_index = len(self.show_collection) - 1
        self.image_index = 0

    def size(self):
        return len(self.show_collection)

    def add_collection(self, name = '', path = '', images: List[str] = [], collection:Collection = None )-> bool:
        
        if collection is not None and collection.valid():
            self.collections.append(collection)
            self.show_collection = self._get_collection_to_show()
            return True
        elif collection is not None:
            return False

        if not path or len(images) == 0 :
            return False
        
        if not name:
            path = name

        self.collections.append(Collection(name,path,images))

        self.show_collection = self._get_collection_to_show()

        return True

    def get_image(self , collection_index=-1, image_index=-1):
        if len(self.show_collection) == 0 or not collection_index < len(self.show_collection):
            return ''

        if collection_index > -1:
            self.collection_index = collection_index

        if image_index > -1:
            self.image_index = image_index

        return self.show_collection[self.collection_index].get_image(self.image_index)

    def get_collection_names(self)->List[str]:
        name_list = []
        for it in self.show_collection:
            name_list.append(it.get_name())
        return name_list

    def toggle_tag_in_collection(self, index, tag):
        if index < len(self.show_collection):
            self.show_collection[index].toggle_tag(tag)

    def _get_collection_to_show(self):
        if len(self.filter_tags) == 0:
            return self.collections
        
        self.show_collection = []
        for item in self.collections:
            in_collection = False
            for tag in self.filter_tags:
                in_collection = in_collection or item.tag_in_collection(tag)
            
            if in_collection:
                self.show_collection.append(item)

        return self.show_collection

    def toggle_tag_filter(self, tag):
        if tag in self.filter_tags:
            self.filter_tags.remove(tag)
        else:
            self.filter_tags.append(tag)
        return self._get_collection_to_show()
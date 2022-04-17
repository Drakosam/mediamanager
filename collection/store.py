from os import listdir
from os.path import isdir, join, isfile
from typing import List


class CollectionStore:
    def __init__(self):
        self.collection: List[CollectionItem] = []
        self.collection_keys = {}

    def setup_collection(self, path):
        self.collection = [CollectionItem(path, f) for f in listdir(path) if isdir(join(path, f))]
        for i, v in enumerate(self.collection):
            self.collection_keys[v.name] = i

    def get_collection_index_by_name(self, name):
        return self.collection_keys[name]

    def get_image_from_collection(self, collection_index, image_index):
        return self.collection[collection_index].get_image(image_index)

    def get_collection_size(self, index):
        return self.collection[index].get_size()

    def get_all_paths_for_collection(self, collection_name):
        index = self.get_collection_index_by_name(collection_name)
        return self.collection[index].get_all_paths()


class CollectionItem:
    def __init__(self, root, name):
        self.name = name
        self.root = root
        self.ready = False
        self.items = []

    def _update(self):
        if not self.ready:
            self.items = [f for f in listdir(join(self.root, self.name)) if isfile(join(self.root, self.name, f))]
            self.ready = True

    def get_image(self, index_image):
        self._update()
        return join(self.root, self.name, self.items[index_image])

    def get_size(self):
        self._update()
        return len(self.items)

    def get_all_paths(self):
        return [join(self.root, self.name, f) for f in self.items]

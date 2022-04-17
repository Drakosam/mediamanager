from collection.store import CollectionStore


class CollectionManage:

    def __init__(self):
        self.store = CollectionStore()
        self.collection_index = 0
        self.image_index = 0
        self.show_index = 0
        self.current_collection_name = ''
        self.collection_in_show = []
        self.image_in_show = []
        self.auto_run = False

    def set_collection_from_dir(self, path):
        self.store.setup_collection(path)
        self.current_collection_name = self.store.collection[self.collection_index].name

    def get_collection_names(self):
        return [i.name for i in self.store.collection]

    def set_collection_by_name(self, c_name):
        self.current_collection_name = c_name
        self.collection_index = self.store.get_collection_index_by_name(c_name)

    def get_image_path(self):
        if len(self.store.collection) == 0:
            return ''
        if not self.auto_run:
            return self.store.get_image_from_collection(self.collection_index, self.image_index)
        else:
            return self.image_in_show[self.show_index]

    def next_image(self):
        self.image_index += 1
        if self.store.get_collection_size(self.collection_index) <= self.image_index:
            self.image_index = 0

    def next_collection(self):
        self.collection_index += 1
        if len(self.store.collection) <= self.collection_index:
            self.collection_index = 0
        self.image_index = 0
        self.current_collection_name = self.store.collection[self.collection_index].name

    def next_in_show(self):
        if len(self.collection_in_show) == 0:
            self.next_image()
        else:
            self.show_index += 1
            if self.show_index >= len(self.image_in_show):
                self.show_index = 0

    def prev_image(self):
        self.image_index -= 1
        if self.image_index < 0:
            self.image_index = self.store.get_collection_size(self.collection_index) - 1

    def prev_collection(self):
        self.collection_index -= 1
        if self.collection_index < 0:
            self.collection_index = len(self.store.collection) - 1
        self.image_index = 0
        self.current_collection_name = self.store.collection[self.collection_index].name

    def tag_ass_part_of_show(self):
        if self.current_collection_name in self.collection_in_show:
            self.collection_in_show.remove(self.current_collection_name)
        else:
            self.collection_in_show.append(self.current_collection_name)

    def start_auto_run(self):
        if len(self.collection_in_show) > 0:
            self.image_in_show = []
            for name in self.collection_in_show:
                self.image_in_show += self.store.get_all_paths_for_collection(name)
        self.auto_run = True
        self.show_index = 0

    def stop_auto_run(self):
        self.auto_run = False

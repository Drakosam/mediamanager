from typing import List
from os import path as os_path

class Collection:
    def __init__(self) -> None:
        self.name = ''
        self.path = ''
        self.tags = []
        self.images = []

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_path(self,path):
        self.path = path

    def get_path(self):
        return self.path

    def toggle_tag(self,tag):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            self.tags.append(tag)

    def tag_in_collection(self,tag):
        return tag in self.tags

    def add_images_list(self,images:List[str]):
        self.images = images

    def get_image(self,nr):
        if nr >= 0 and nr < len(self.images):
            return os_path.join(self.path,self.images[nr])  
        else:
            return ''

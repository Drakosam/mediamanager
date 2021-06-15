from typing import List
from os import name, path as os_path

class Collection:
    def __init__(self, name: str= '', path: str= '', images: List[str] =[]) -> None:
        self.name = name
        self.path = path
        self.images = images
        self.tags: List[str] = []

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_path(self, path: str):
        self.path = path

    def get_path(self) -> str:
        return self.path

    def toggle_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            self.tags.append(tag)

    def tag_in_collection(self, tag: str) -> bool:
        return tag in self.tags

    def add_images_list(self, images: List[str]):
        self.images = images

    def get_image(self, nr: int) -> str:
        if nr >= 0 and nr < len(self.images):
            return os_path.join(self.path, self.images[nr])  
        else:
            return ''

    def valid(self)-> bool:
        if self.name  and self.path  and len(self.images)> 0:
            return True

        return False 
        
    def size(self):
        return len(self.images)
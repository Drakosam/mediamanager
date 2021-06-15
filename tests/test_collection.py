import os
from utility import collection
from utility.collection import Collection


def test_colection_name():
    collection_name= "test_collection_name"

    test_item = Collection()
    test_item.set_name(collection_name)
    
    assert test_item.get_name() == collection_name

def test_collection_path():
    collection_path = "C:\\path\\path1\\path2"
    test_item = Collection()
    test_item.set_path(collection_path)

    assert test_item.get_path() == collection_path

def test_collection_add_tag():
    test_item = Collection()
    test_item.toggle_tag('tag_1')
    test_item.toggle_tag('tag_2')
    test_item.toggle_tag('tag_3')

    assert test_item.tag_in_collection('tag_1')
    assert test_item.tag_in_collection('tag_2')
    assert test_item.tag_in_collection('tag_3')
    assert not test_item.tag_in_collection('tag_4')


def test_collection_tag_toggle():
    test_item = Collection()
    
    test_item.toggle_tag('tag_1')
    test_item.toggle_tag('tag_2')
    test_item.toggle_tag('tag_1')

    assert not test_item.tag_in_collection('tag_1')
    assert test_item.tag_in_collection('tag_2')


def test_collection_images_path():
    test_item = Collection()
    path="long_path"
    image_list = ['img1','img2','img3']
    test_item.set_path(path)
    test_item.add_images_list(image_list)
    
    assert test_item.get_image(0) == os.path.join(path,image_list[0])
    assert test_item.get_image(1) == os.path.join(path,image_list[1])
    assert test_item.get_image(2) == os.path.join(path,image_list[2])

def test_collection_image_overflow():
    test_item = Collection()
    path="long_path"
    image_list = ['img1','img2','img3']
    test_item.set_path(path)
    test_item.add_images_list(image_list)

    assert test_item.get_image(100) == ''


def test_collection_is_valid():
    test_item_1 = Collection(name='', path='',images=[])
    test_item_2 = Collection(name='', path='path',images=['image'])
    test_item_3 = Collection(name='name', path='',images=['image'])
    test_item_4 = Collection(name='name', path='path',images=[])
    test_item_5 = Collection(name='name', path='path',images=['image'])

    assert not test_item_1.valid()
    assert not test_item_2.valid()
    assert not test_item_3.valid()
    assert not test_item_4.valid()
    assert test_item_5.valid()

def test_collection_size_return_numer_of_images():
    test_item_1 = Collection(name='name1', path='path1',images=['image_1_1'])
    test_item_2 = Collection(name='name2', path='path2',images=['image_2_1','image_2_2'])
    test_item_3 = Collection(name='name3', path='path3',images=['image_3_1','image_3_2','image_3_3'])

    assert test_item_1.size() == 1
    assert test_item_2.size() == 2
    assert test_item_3.size() == 3

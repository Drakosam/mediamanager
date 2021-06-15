from os import path
import os
from utility import collection
from utility.collection_manager import CollectionManager
from utility.collection import Collection


def test_collection_manager_new_item_size_is_0():
    test_item = CollectionManager()

    assert test_item.size() == 0


def test_collection_manager_add_new_collection_item_by_obj():
    test_collection_1 = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2 = Collection('222','path2',['img_2_1','img_2_2','img_2_3'])
    test_collection_3 = Collection('333','path3',['img_3_1','img_3_2','img_3_3'])

    test_item = CollectionManager()

    test_item.add_collection(collection=test_collection_1)
    test_item.add_collection(collection=test_collection_2)
    test_item.add_collection(collection=test_collection_3)

    assert test_item.size() == 3


def test_collection_manager_add_new_collection_item_by_values():


    test_item = CollectionManager()

    test_item.add_collection(name= '111', path='path1',images=['img_1_1','img_1_2','img_1_3'])
    test_item.add_collection('222', 'path2',['img_2_1','img_2_2','img_2_3'])
    test_item.add_collection(name= '333', path='path3',images=['img_3_1','img_3_2','img_3_3'])

    assert test_item.size() == 3


def test_collection_manager_add_new_collection_item_only_if_is_valid():
    test_collection_1_valid = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2_not_valid = Collection('222','',['img_2_1','img_2_2','img_2_3'])


    test_item = CollectionManager()

    result_1=test_item.add_collection(collection=test_collection_1_valid)
    result_2=test_item.add_collection(collection=test_collection_2_not_valid)
    result_3=test_item.add_collection(name= '333', path='path3',images=['img_3_1','img_3_2','img_3_3'])
    result_4=test_item.add_collection(name= '444', path='path4',images=[])

    assert test_item.size() == 2
    assert result_1
    assert not result_2
    assert result_3
    assert not result_4

def test_collection_manager_get_image_retur_empty_string_when_collections_are_empty():
    test_item = CollectionManager()

    assert test_item.get_image() == ''

def test_collection_manager_get_image_retur_by_defalut_first_image_of_first_collection():
    test_item = CollectionManager()

    test_collection_1 = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2 = Collection('222','path2',['img_2_1','img_2_2','img_2_3'])
    test_collection_3 = Collection('333','path3',['img_3_1','img_3_2','img_3_3'])
    test_item.add_collection(collection=test_collection_1)
    test_item.add_collection(collection=test_collection_2)
    test_item.add_collection(collection=test_collection_3)

    assert test_item.get_image() == test_collection_1.get_image(0)


def test_collection_manager_get_image_allow_pick_collection_by_index():
    test_item = CollectionManager()

    test_collection_1 = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2 = Collection('222','path2',['img_2_1','img_2_2','img_2_3'])
    test_collection_3 = Collection('333','path3',['img_3_1','img_3_2','img_3_3'])
    test_item.add_collection(collection=test_collection_1)
    test_item.add_collection(collection=test_collection_2)
    test_item.add_collection(collection=test_collection_3)

    assert test_item.get_image(collection_index=1) == test_collection_2.get_image(0)


def test_collection_manager_get_image_allow_pick_image_in_collection_by_index():
    test_item = CollectionManager()

    test_collection_1 = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2 = Collection('222','path2',['img_2_1','img_2_2','img_2_3'])
    test_collection_3 = Collection('333','path3',['img_3_1','img_3_2','img_3_3'])
    test_item.add_collection(collection=test_collection_1)
    test_item.add_collection(collection=test_collection_2)
    test_item.add_collection(collection=test_collection_3)

    assert test_item.get_image(image_index=1) == test_collection_1.get_image(1)


def test_collection_manager_get_image_allow_pick_image_and_collection_by_index():
    test_item = CollectionManager()

    test_collection_1 = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2 = Collection('222','path2',['img_2_1','img_2_2','img_2_3'])
    test_collection_3 = Collection('333','path3',['img_3_1','img_3_2','img_3_3'])
    test_item.add_collection(collection=test_collection_1)
    test_item.add_collection(collection=test_collection_2)
    test_item.add_collection(collection=test_collection_3)

    assert test_item.get_image(image_index=1,collection_index=1) == test_collection_2.get_image(1)


def test_collection_manager_get_image_overflow_pick_image_in_collection_by_index_return_empty_string():
    test_item = CollectionManager()

    test_collection_1 = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2 = Collection('222','path2',['img_2_1','img_2_2','img_2_3'])
    test_collection_3 = Collection('333','path3',['img_3_1','img_3_2','img_3_3'])
    test_item.add_collection(collection=test_collection_1)
    test_item.add_collection(collection=test_collection_2)
    test_item.add_collection(collection=test_collection_3)

    assert test_item.get_image(image_index=100,collection_index=1) == ''

def test_collection_manager_get_image_overflow_pick_collection_by_index_return_empty_string():
    test_item = CollectionManager()

    test_collection_1 = Collection('111','path1',['img_1_1','img_1_2','img_1_3'])
    test_collection_2 = Collection('222','path2',['img_2_1','img_2_2','img_2_3'])
    test_collection_3 = Collection('333','path3',['img_3_1','img_3_2','img_3_3'])
    test_item.add_collection(collection=test_collection_1)
    test_item.add_collection(collection=test_collection_2)
    test_item.add_collection(collection=test_collection_3)

    assert test_item.get_image(image_index=1,collection_index=100) == ''
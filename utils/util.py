import json
from HW1 import Category, Product


def get_data():
    """ Читаем файл данных"""
    with open("products2.json", encoding="utf-8") as f:
        data = json.load(f)
        return data


def quantity_category():
    len_cat = len(get_data()) #считаем количество категорий
    print(f'Количество категорий: {len_cat}')



Category(get_data())



quantity_category()
print(get_data())


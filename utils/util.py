import json
from HW_1 import Category
from HW_1 import Product

def get_data():
    """ Читаем файл данных"""
    with open("products.json", encoding="utf-8") as f:
        data = json.load(f)
        return data

def quantity_category():
    x = len(get_data()) #считаем количество категорий
    print(f'Количество категорий: {x}')

quantity_category()


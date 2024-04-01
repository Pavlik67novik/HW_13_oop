import pytest

from HW_1 import Category
from HW_1 import Product

@pytest.fixture()
def Category_phone():
    return Category('Телефоны', "Мобильные телефоны", "Apple")

def test_init(Category_phone):
    assert Category_phone.name == 'Телефоны'
    assert Category_phone.description == 'Мобильные телефоны'
    assert Category_phone.products == 'Apple'

@pytest.fixture()
def Product_phone():
    return Product('Iphone12', "new iphone", 58000, 2)


def Product_init(Product_phone):
    assert Product_phone.name == 'Iphone12'
    assert Product_phone.description == 'new iphone'
    assert Product_phone.price == 58000
    assert Product_phone.quantity_in_stock == 2
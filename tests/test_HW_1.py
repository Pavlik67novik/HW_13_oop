import pytest


from utils.HW1 import Category, Product



@pytest.fixture()
def Category_phone():
    prod = ("iphone 11", "iphone 13", "iphone 12")
    return Category('Сотовые телефоны', "Смартфоны", prod)

def test_init(Category_phone):
    assert Category_phone.name == 'Сотовые телефоны'
    assert Category_phone.description == 'Смартфоны'
    assert Category_phone.products[0] == 'iphone 11'
    assert Category_phone.product_count == 3
    assert Category_phone.category_count == 1


@pytest.fixture()
def Product_phone():
    return Product('Iphone12', "new iphone", 58000, 2)


def Product_init(Product_phone):
    assert Product_phone.name == 'Iphone12'
    assert Product_phone.description == 'new iphone'
    assert Product_phone.price == 58000
    assert Product_phone.quantity_in_stock == 2


import pytest


from utils.HW1 import Category, Product



@pytest.fixture()
def Category_phone():
    products = [Product('Iphone11', "new iphone", 28000, 3), Product('Iphone12', "new iphone", 38000, 4), Product('Iphone13', "new iphone", 58000, 2)]
    return Category('Сотовые телефоны', "Смартфоны", products)

def test_init(Category_phone):
    assert Category_phone.name == 'Сотовые телефоны'
    assert Category_phone.description == 'Смартфоны'
    assert Category_phone.product_count == 3
    assert Category_phone.category_count == 1
    assert len(Category_phone.products) == 3
    assert Category_phone.category_count == 1


@pytest.fixture()
def Product_phone():
    return Product('Iphone12', "new iphone", 58000, 2)


def test_Product_init(Product_phone):
    assert Product_phone.name == 'Iphone12'
    assert Product_phone.description == 'new iphone'
    assert Product_phone.price == 58000
    assert Product_phone.quantity_in_stock == 2


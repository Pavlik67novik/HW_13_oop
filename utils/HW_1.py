class Category:
    name: str #Название
    description: str #Описние
    products: str # товары



    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.quantity_category = quantity_category # Кол-во категорий
        self.unique_product = unique_product  # Кол-во уникальных продуктов


class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


if __name__ == "__main__":
    r1 = Category('iphone12', "Cool phone", "Дорогие телефоны")
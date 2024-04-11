class Category:
    """   Класс для категорий товара   """
    name: str #Название
    description: str #Описние
    products: str # товары
    category_count = 0
    product_count = 0



    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(set(self.products))


    def add_products(self, value):
        self.__products.append(value)
        Category.product_count += 1



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


#if __name__ == "__main__":
    #r1 = Category('iphone12', "Cool phone", "Дорогие телефоны")
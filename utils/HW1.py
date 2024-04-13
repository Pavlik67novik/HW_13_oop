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



    @property
    def products(self):
        return self.__products


    @property
    def list_product(self):
        output = ''
        for product in self.__products:
            output += f'{product.name},{product.price} руб. Остаток {product.count} шт.\n'
        return output


    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return quantity

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


    @classmethod
    def creat_poducts(cls, **kwargs):
        return cls(name, description, price, quantity_in_stock)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity_in_stock}'



    def __add__(self, other):
        """Метод сложения сумм и умножения на кол-во на складе"""
        return (self.price * self.quantity_in_stock) + (other.price * other.quantity_in_stock)

# if __name__ == "__main__":
#     #t1 = {'name' : 'iphone12', 'description' : "smartphone", 'price' : 58400, 'quantity_in_stock' : 15}
#     t1 = Product('iphone12', "smartphone", 58400, 15)
#     #prod = creat_poducts(t1)
#     print(t1)
from abc import ABC, abstractmethod


class MixinRepr:

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.__dict__.items()})'

class ZeroQuantityException(Exception):
    """ вызов сообщения ошибки при кол-ве = 0 """
    def __init__(self, message="Попытка добавить товар с нулевым количеством.") -> None:
        self.message = message
        super().__init__(self.message)



class AbstractProduct(ABC):

    @classmethod
    @abstractmethod
    def creat_product(cls):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass


class Category(MixinRepr):
    """   Класс для категорий товара   """
    # наследуем от абстрактного класса  MixinRepr
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
        super().__repr__()

    def add_products(self, product, quantity_in_stock):
        if quantity_in_stock > 0:
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("КОл-во должно быть больше  0")


    def average_price(self):
        """Метод, который подсчитывает средний ценник всех товаров """
        average_price = []
        for goods in self.__products:
            try:
                total_price = sum(product.price for product in self.products)
                average_price = total_price / len(self.products)
            except ZeroDivisionError:
                return 0
            return average_price
        #         if goods.quantity == 0:
        #             raise ZeroDivisionError
        #         average_price.append(goods.price)
        #     except ZeroDivisionError:
        #         return 0
        # return sum(average_price) / len(average_price)


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


    def zero_quantity(self, quantity):
        if quantity < 1:
            raise ValueError

class Product(MixinRepr, AbstractProduct):
    #наследуем от абстрактного класса  MixinRepr
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        if quantity_in_stock == 0:
            raise ZeroQuantityException() #сразу на входных данных проверяем, и выводим в ошибку если Try
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        super().__repr__()


    @classmethod
    def creat_product(cls, **kwargs):
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
        if type(self) is type(other):
            return (self.price * self.quantity_in_stock) + (other.price * other.quantity_in_stock)
        raise TypeError
        # if isinstance(other, type(self)):
        #     return (self.price * self.quantity_in_stock) + (other.price * other.quantity_in_stock)
        # else:
        #     raise TypeError




class Smartphone(Product):
    """ Создаем класс смартфон наследуемый от Продукта"""

    def __init__(self, efficiency, model, memory, colour, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.colour = colour


class Lawn_grass(Product):
    """ Создаем класс трава_газон наследуемый от Продукта"""

    def __init__(self, country, period, colour, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.colour = colour





# if __name__ == "__main__":
#     #t1 = {'name' : 'iphone12', 'description' : "smartphone", 'price' : 58400, 'quantity_in_stock' : 15}
#     t1 = Product('iphone12', "smartphone", 58400, 0)
#     prod = creat_poducts(t1)
#     print(t1)

# t1 = Product('iphone12', "smartphone", 58400, 2)
# # Создаем объект класса Category
# category = Category('telefons', 'smarfon', t1)
#
# # Пытаемся добавить продукт с количеством товаров > 0
# try:
#     category.add_products("Product 1", 5)
#     print("Product added successfully")
# except ValueError as e:
#     print(f"Error: {e}")
#
# # Пытаемся добавить продукт с количеством товаров = 0
# try:
#     category.add_products("Product 2", 0)
#     print("Product added successfully")
# except ValueError as e:
#     print(f"Error: {e}")
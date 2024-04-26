from abc import ABC, abstractmethod


class MixinRepr:

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.__dict__.items()})'

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

    def add_products(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        #self.__products.append(value)
        #Category.product_count += 1



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

class Product(MixinRepr, AbstractProduct):
    #наследуем от абстрактного класса  MixinRepr
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        super().__repr__()


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



# if __name__ == "__main__":
#     #t1 = {'name' : 'iphone12', 'description' : "smartphone", 'price' : 58400, 'quantity_in_stock' : 15}
#     t1 = Product('iphone12', "smartphone", 58400, 15)
#     #prod = creat_poducts(t1)
#     print(t1)
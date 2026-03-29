class Product:
    def __init__(self, price):
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price


product = Product(10)
product.price = 15
print(product.price)

class Person:
    def __init__(self, fullname):
        self.__fullname = fullname
    
    @property
    def fullname(self):
        return self.__fullname
    
person = Person("Mehdi Karimi")
#person.fullname = "Ali Karimi" raises attribute error
person.__fullname = "Ali Karimi" #Does not change fullname and create a dynamic attribute with __fullname
print(person.fullname)
print(person.__fullname)
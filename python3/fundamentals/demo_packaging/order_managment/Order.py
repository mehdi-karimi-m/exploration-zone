import uuid

class Order:
    def __init__(self, id, customer, instrument, quantity, price, side):
        self.id = id
        self.customer_id = customer.id
        self.instrument_id = instrument.id
        self.quantity = quantity
        self.price = price
        self.side = side

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customer_id = customer_id

    @property
    def instrument_id(self):
        return self.__instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        self.__instrument_id = instrument_id

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side

    @classmethod
    def place(cls, customer, instrument, quantity, price, side):
        return cls(uuid.uuid4(), customer, instrument, quantity, price, side)
    
    def get_value(self):
        return self.quantity * self.price

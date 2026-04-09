#from ..framework.invalid_operation_error import InvalidOperationError
from demo_packaging.framework.invalid_operation_error import InvalidOperationError


class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id == "" or id is None:
            raise ValueError("account id cannot be empty.")
        self.__id = id


    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise InvalidOperationError("account balance cannot be empty.")
        self.__balance = balance

    @classmethod
    def open(cls, id):
        return cls(id, 0)
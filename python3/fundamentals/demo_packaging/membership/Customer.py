class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id == "" or id is None:
            raise ValueError("id cannot be empty.")
        self.__id = id

    @property
    def first_name(self):        
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name == "" or first_name is None:
            raise ValueError("first name cannot be empty")
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name == "" or last_name is None:
            raise ValueError("last name cannot be empty")
        self.__last_name = last_name

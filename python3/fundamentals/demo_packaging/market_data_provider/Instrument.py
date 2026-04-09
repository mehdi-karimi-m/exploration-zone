class Instrument:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if id == "" or id is None:
            raise ValueError("instrument id cannot be empty or none.")
        self.__id = id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title == "" or title is None:
            raise ValueError("instrument title cannot be empty or none.")
        self.__title = title

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    """This a custom exception for rasing on invalid operations."""


class Stream(ABC):
    """Defining an abstraction for working by any streams."""
    def __init__(self):
        super().__init__()
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):    
    def read(self):
        if not self.opened:
            raise InvalidOperationError(
                "Cannot read from stream when is not open")
        print("Reading from file stream.")


class NetworkStream(Stream):
    def read(self):
        if not self.opened:
            raise InvalidOperationError(
                "Cannot read from stream when is not open")
        print("Reading from network stream.")


class MemoryStream(Stream):
    pass
    # def read(self):
    #     if not self.opened:
    #         raise InvalidOperationError(
    #             "Cannot read from stream when is not open")
    #     print("Reading from memory stream.")


file_stream = FileStream()
file_stream.open()
file_stream.read()

memory_stream = MemoryStream()
memory_stream.open()
memory_stream.read()

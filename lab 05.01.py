"""This IS Class"""
class DataNode:
    """DaTaNoDe"""
    def __init__(self, data=None):
        """Docstring"""
        self.__data = data
        self.__next = None

    def get_data(self):
        """GO Get data"""
        return self.__data

    def set_data(self, data):
        """Set"""
        self.__data = data

    def get_next(self):
        """next"""
        return self.__next

    def set_next(self, next_):
        """set"""
        self.__next = next_

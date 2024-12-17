"""BSTNode"""
class BSTNode:
    """BSTNode"""
    def __init__(self, data):
        """Atribute"""
        self.__data = data
        self.__left = None
        self.__right = None

    def set_data(self, data):
        """Set"""
        self.__data = data

    def get_data(self):
        """GO Get data"""
        return self.__data

    def set_left(self, left):
        """Setter"""
        self.__left = left

    def get_left(self):
        """Getter"""
        return self.__left

    def set_right(self, right):
        """Setter"""
        self.__right = right

    def get_right(self):
        """Getter"""
        return self.__right

def main():
    """This main"""
    p_new = BSTNode(int(input()))
    print(p_new.get_data())
    print(p_new.get_left())
    print(p_new.get_right())
main()

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

class SinglyLinkedList():
    """SinglyLinkedList_Class"""
    def __init__(self):
        """Attribute"""
        self.count = 0
        self.head = None

    def traverse(self):
        """Traverse"""
        result = ""
        pos = self.head
        if pos is None:
            print("This is an empty list.")
        else:
            while pos is not None:
                result += pos.get_data() + " -> "
                pos = pos.get_next()
            print(result.rstrip(" -> "))

    def insert_last(self, data):
        """INserting NOdes Into An ordered LIst"""
        pnew = DataNode(data)
        if self.head is None:
            self.head = pnew
        else:
            start = self.head
            while start.get_next() is not None:
                start = start.get_next()
            start.set_next(pnew)
        self.count += 1

def main():
    """Main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()

"""Singly Linked List (Delete)"""
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

    def insert_front(self, data):
        """INserting"""
        pnew = DataNode(data)
        pnew.set_next(self.head)
        self.head = pnew
        self.count += 1

    def insert_before(self, node, data):
        """www"""
        start = self.head
        prev = None
        while (start is not None) and (start.get_data() != node):
            prev = start
            start = start.get_next()
        if start is None:
            print("Cannot insert, %s does not exist." %node)
        else:
            pnew = DataNode(data)
            if prev is None:
                pnew.set_next(self.head)
                self.head = pnew
            else:
                pnew.set_next(start)
                prev.set_next(pnew)
            self.count += 1
    def delete(self, data):
        """Delete not help to forget"""
        prev = None
        start = self.head
        while start is not None and start.get_data() != data:
            prev = start
            start = start.get_next()
        if start is None:
            print("Cannot delete, %s does not exist." %data)
        else:
            if prev is None:
                self.head = start.get_next()
            elif start.get_next() is None:
                prev.set_next(None)
            else:
                prev.set_next(start.get_next())
            del start
            self.count -= 1

def main():
    """Main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()

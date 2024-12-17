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

class BST:
    """BST Not BTS"""
    def __init__(self):
        self.root = None

    def get_root(self):
        """Getter"""
        return self.root

    def insert(self, data):
        """Insert"""
        pnew = BSTNode(data)
        root = self.root
        if root is None:
            self.root = pnew
        else:
            start = root
            while start is not None:
                prev = start #กำหนดตัวก่อนหน้าเป็นรูท
                if data < start.get_data():
                    start = start.get_left() #ถ้าดาต้าน้อยกว่า รูทให้กำหนด สตาร์ทเปนตัวทางซ้าย
                else:
                    start = start.get_right() #ถ้าดาต้ามากกว่า รูทให้กำหนด สตาร์ทเปนตัวทางขวา
            if pnew.get_data() < prev.get_data():
                prev.set_left(pnew)
            else:
                prev.set_right(pnew)

    def delete(self, data):
        if self.root is None:
            return None
        start = self.root
        prev = None
        while start is not None and start.get_data() != data:
            prev = start
            if data < start.get_data():
                start = start.get_left()
            else:
                start = start.get_right()

        if start is None:
            print("Delete Error, %s is not found in Binary Search Tree." % data)
            return None

        if start.get_left() is None:
            if prev is None:
                self.root = start.get_right()
            elif prev.get_left() == start:
                prev.set_left(start.get_right())
            else:
                prev.set_right(start.get_right())

        elif start.get_right() is None:
            if prev is None:
                self.root = start.get_left()
            elif prev.get_right() == start:
                prev.set_right(start.get_left())
            else:
                prev.set_left(start.get_left())

        else:
            my_sub3 = start.get_left()
            pointer = start
            while my_sub3.get_right() is not None:
                pointer = my_sub3
                my_sub3 = my_sub3.get_right()

            if pointer.get_left() == my_sub3:
                pointer.set_left(my_sub3.get_left())
            else:
                pointer.set_right(my_sub3.get_left())
            start.set_data(my_sub3.get_data()) # ตั้งสาร์ทเป็นตัวฝั่งซ้ายที่มากที่สุด

    def find_min(self):
        """min"""
        if self.is_empty():
            return None
        else:
            root = self.root
            temp = None
            while root is not None:
                temp = root
                root = root.get_left()
            return temp.get_data()

    def find_max(self):
        """max"""
        if self.is_empty():
            return None
        else:
            root = self.root
            temp = None
            while root is not None:
                temp = root
                root = root.get_right()
            return temp.get_data()

    def is_empty(self):
        """M T"""
        return self.root is None

    def inorder(self, root):
        """In 0rder"""
        if root is not None:
            self.inorder(root.get_left())
            print("->", root.get_data(), end=" ")
            self.inorder(root.get_right())

    def postorder(self, root):
        """In 0rder"""
        if root is not None:
            self.postorder(root.get_left())
            self.postorder(root.get_right())
            print("->", root.get_data(), end=" ")

    def preorder(self, root):
        """preorder"""
        if root is not None:
            print("->", root.get_data(), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

    def traverse(self):
        """Traverse"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder(self.get_root())
        print()
        print('Inorder: ', end='')
        self.inorder(self.get_root())
        print()
        print('Postorder: ', end='')
        self.postorder(self.get_root())

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()

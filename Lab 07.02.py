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

    def preorder(self, root):
        """preorder"""
        if root is not None:
            print("->", root.get_data(), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

def main():
    """main"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder(my_bst.get_root())
main()

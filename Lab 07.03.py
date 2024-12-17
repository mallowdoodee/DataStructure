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
    """Main"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())
main()

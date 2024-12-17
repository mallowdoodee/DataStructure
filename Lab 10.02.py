"""Labs 10.02"""
class Student:
    """Labs 10.01"""
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self):
        return self.__std_id

    def get_name(self):
        return self.__name

    def get_gpa(self):
        return self.__gpa

    def print_details(self):
        print("ID:", self.get_std_id())
        print("Name:", self.get_name())
        print("GPA: %.2f" % self.get_gpa())

class ProbHash:
    """Labs 10.02"""
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size
    def hash(self, key):
        return key % self.size
    
    def rehash(self, key):
        return (key + 1)
    
    def insert_data(self, student):
        index = self.hash(student.get_std_id())
        if self.hash_table[index] is None:
            self.hash_table[index] = [student.get_std_id(), student.get_name(), student.get_gpa()]
            print("Insert " + str(student.get_std_id()), "at index", str(index))
        else:
            box = False #Full List
            index_ = self.rehash(index)
            for _ in range(self.size):
                index_ %= self.size
                if self.hash_table[index_] is None:
                    box = True
                    self.hash_table[index_] = [student.get_std_id(), student.get_name(), student.get_gpa()]
                    print("Insert " + str(student.get_std_id()) + " at index " + str(index_))
                    break
                index_ = self.rehash(index_)
            if box == False:
                print("The list is full. %s could not be inserted." % str(student.get_std_id()))

    def search_data(self, std_id):
        """search data"""
        for i in range(self.size):
            if self.hash_table[i] is not None and str(self.hash_table[i][0]) == str(std_id):
                print("Found " + str(std_id) + " at index " + str(i))
                return Student(self.hash_table[i][0], self.hash_table[i][1], self.hash_table[i][2])
        print(str(std_id) + " does not exist.")

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
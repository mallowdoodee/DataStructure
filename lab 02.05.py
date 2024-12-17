"""lab"""
class ArrayStack:
    """lab 2 pb.5"""
    def __init__(self):
        """attibutes"""
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def is_empty(self):
        """mt"""
        return not self.size > 0

    def pop(self):
        """Nayeon"""
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            self.size -= 1
            return self.data.pop()

    def get_stack_top(self):
        """get"""
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            return self.data[-1]

    def get_size(self):
        """real beauty"""
        return self.size

    def print_stack(self):
        """output"""
        print(self.data)

def is_parentheses_matching(equation):
    """Main Parentheses Matching"""
    temp = ArrayStack()
    underflow = False
    for i in equation:
        if i == "(":
            temp.push(i)
        elif i == ")":
            if temp.pop() == None:
                underflow = True
    if temp.is_empty() and not underflow:
        print("Parentheses in %s are matched" % equation)
        return True
    else:
        print("Parentheses in %s are unmatched" % equation)
        return False
print(is_parentheses_matching(input()))

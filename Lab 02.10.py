"""lab"""
class ArrayStack:
    """02"""
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

STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())

print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)

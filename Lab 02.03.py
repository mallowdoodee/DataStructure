"""lab-Student Group"""
class ArrayStack:
    """Student group"""
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

def distribute_students():
    """Main"""
    num_groups = int(input())
    pupil = int(input())
    students = []
    for i in range(pupil):
        students.append(input())

    student_stack = ArrayStack()

    for student in students:
        student_stack.push(student)

    groups = [[] for _ in range(num_groups)]

    while not student_stack.is_empty():
        for group in groups:
            student = student_stack.pop()
            if student is not None:
                group.append(student)

    for i, group in enumerate(groups, 1):
        print("Group %d: %s" %(i, ', '.join(group)))
distribute_students()

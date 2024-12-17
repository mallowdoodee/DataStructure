"""Lab 01.06"""
class Elevator:
    """Classy"""
    def __init__(self, max_floor):
        """Lab 01.06"""
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """Lab 01.06"""
        floor = int(floor)
        if floor > self.max_floor:
            return "Invalid Floor!"
        else:
            self.current_floor = floor
            return floor

    def report_current_floor(self):
        """Report"""
        return self.current_floor

def main():
    """This is MAIN"""
    elevator = Elevator(int(input()))
    while True:
        current_floor = input()
        if current_floor.lower() == "done":
            print(elevator.report_current_floor())
            break
        else:
            if elevator.go_to_floor(current_floor) == "Invalid Floor!":
                print("Invalid Floor!")
main()

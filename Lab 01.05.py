"""Lab 01.05"""
class Point:
    """Lab 01.05"""
    def __init__(self, myx=0, myy=0):
        """Lab 01.05"""
        self.set_coordinates(myx, myy)
    def set_coordinates(self, myx, myy):
        """Lab 01.05"""
        self.myx = myx
        self.myy = myy
    def calculate_distance(self, other_point):
        """Lab 01.05"""
        return ((other_point.myx - self.myx)**2 + (other_point.myy - self.myy)**2) ** 0.5

def main():
    """Lab 01.05"""
    art = Point(float(input()), float(input()))
    boss = Point(float(input()), float(input()))
    print("%.2f" % boss.calculate_distance(art))
main()

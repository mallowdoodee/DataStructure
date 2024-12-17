"""Exercise 00.02"""
def drying():
    """Exercise 00.02"""
    insideout = input()
    timimg = float(input())
    if insideout == "Indoor":
        if timimg >= 480:
            print("True")
        else:
            print("False")
    else:
        if timimg >= 240:
            print("True")
        else:
            print("False")
drying()

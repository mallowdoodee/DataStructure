"""Lab 01.01 - Is_Even"""
def is_even():
    """Lab 01.01 - Is_Even"""
    num = list(input())
    even = [2, 4, 6, 8, 0]
    if int(num[-1]) in even:
        print(True)
    else:
        print(False)
is_even()

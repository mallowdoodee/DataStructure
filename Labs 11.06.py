import json
"""Labs 11.06"""
def seatsnumber():
    """Labs 11.06 Bubble Sort"""
    mylist = json.loads(input())
    last = int(input())
    c = 0
    status = False
    count = 0
    while c <= last and status is False:
        w = last
        status = True
        while w > c:
            if ord((mylist[w])[0]) == ord((mylist[w - 1])[0]):
                if int((mylist[w])[1:]) < int((mylist[w - 1])[1:]):
                    status = False
                    mylist[w], mylist[w - 1] = mylist[w - 1], mylist[w]
            elif ord((mylist[w])[0]) < ord((mylist[w - 1])[0]):
                status = False
                mylist[w], mylist[w - 1] = mylist[w - 1], mylist[w]
            count += 1
            w -= 1
        print(mylist)
        c += 1
    print("Comparison times:", count)
seatsnumber()
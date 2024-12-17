import json
"""Labs 11.04"""
def seatsnumber():
    """lab 11.4 Insertion Sort"""
    mylist = json.loads(input())
    last = int(input())
    current = 1
    count = 0
    for current in range(1, last+1):
        hold = mylist[current]
        walker = current - 1
        while True:
            if walker < 0 or (ord(hold[0]) > ord(mylist[walker][0])):
                break
            if hold[0] == (mylist[walker])[0]:
                if int(hold[1:]) >= int(mylist[walker][1:]):
                    break
            mylist[walker+1] = mylist[walker]
            walker -= 1
            count += 1
        mylist[walker+1] = hold
        count += 1
        current += 1
        print(mylist)
        if walker < 0:
            count -= 1
    print("Comparison times:", count)
seatsnumber()

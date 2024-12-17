import json
"""Labs 11.05"""
def seatsnumber():
    """Labs 11.05 Selection Sort"""
    mylist = json.loads(input())
    last = int(input())
    count = 0
    current = 0
    while True:
        if current == last:
            break
        hold = current
        walker = hold + 1
        while True:
            if walker > last:
                break
            word_walker = mylist[walker]
            word_hold = mylist[hold]
            if ord(word_walker[0]) == ord(word_hold[0]):
                if int(word_walker[1:]) < int(word_hold[1:]):
                    hold = walker
            elif ord(word_walker[0]) < ord(word_hold[0]):
                hold = walker
            walker += 1
            count += 1
        mylist[current], mylist[hold] = mylist[hold], mylist[current]
        print(mylist)
        current += 1
    print("Comparison times:", count)
seatsnumber()
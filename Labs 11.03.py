import json
"""Labs 11.03"""
def bubbleSort():
    """Labs 11.03 """
    arr = json.loads(input())
    last = int(input())
    current = 0
    count = 1
    sorted = False
    while current <= last and not sorted:
        walker = last
        sorted = True
        while walker > current:
            if arr[walker] < arr[walker - 1]:
                sorted = False
                arr[walker], arr[walker - 1] = arr[walker - 1], arr[walker]
            count += 1
            walker -= 1
        current += 1
        print(arr)
    print("Comparison times:", count-1)
bubbleSort()


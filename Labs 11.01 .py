import json
def insertSort():
    """insertion"""
    arr = json.loads(input())
    last = int(input())
    current = 1
    count = 0
    while current <= last:
        hold = arr[current]
        walker = current - 1
        while walker >= 0 and hold < arr[walker]:
            arr[walker + 1] = arr[walker]
            walker -= 1
            count += 1
        if hold >= arr[walker] and walker != -1:
            count += 1
        arr[walker + 1] = hold
        current += 1
        print(arr)
    print("Comparison times:", count)
insertSort()
"""[23, 78, 45, 8, 32, 56] , hold = 78 walker = 0 current = 1
[23, 78, 45, 8, 32, 56] , hold = 45 current = 2
[23, 45, 78, 8, 32, 56]
[23, 45, 78, 8, 32, 56]"""

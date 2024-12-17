import json
"""Labs 11.02"""
def selectionSort():
    """Labs 11.02"""
    arr = json.loads(input())
    last = int(input())
    current = 0
    count = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if arr[walker] < arr[smallest]:
                smallest = walker
            walker += 1
            count += 1
        arr[current], arr[smallest] = arr[smallest], arr[current]
        current += 1
        print(arr)
    print("Comparison times:", count)
selectionSort()

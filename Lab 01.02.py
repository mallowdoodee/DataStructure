"""01.02"""
def reverse():
    """01.02"""
    import json
    my_list = json.loads(input())
    for i in range(len(my_list)):
        for j in range(0, len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    result = (my_list[-1], my_list[0], round((sum(my_list) / len(my_list)), 2))
    print(result)
reverse()

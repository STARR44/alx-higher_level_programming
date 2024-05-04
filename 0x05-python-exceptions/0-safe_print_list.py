#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    count = 0
    try:
        for index, element in enumerate(my_list):
            if index == x:
                break
            print("{}".format(element), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count

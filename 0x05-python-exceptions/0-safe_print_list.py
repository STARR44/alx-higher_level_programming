#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index, element in enumerate(my_list):
            if index < x:
                print("{}".format(element), end="")
    except IndexError:
        pass
    print()
    return(index) + 1

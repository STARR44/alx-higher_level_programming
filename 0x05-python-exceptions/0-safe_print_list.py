#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no_count = 0
    try:
        for i, element in enumerate(my_list):
            if no_count < x:
                print("{}".format(element), end="")
                no_count += 1
    except ValueError:
        pass
    print()
    return(no_count)

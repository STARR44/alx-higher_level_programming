#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nocount = 0
    try:
        for i, element in enumerate(my_list):
            if nocount < x:
                print("{}" .format(element), end="")
                nocount += 1
    except IndexError:
        pass
    print()
    return(nocount)

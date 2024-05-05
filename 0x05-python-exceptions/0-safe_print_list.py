#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for index in range(my_list[x:])
        try:
            print("{}".format(my_list[index]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
        print()
        return count

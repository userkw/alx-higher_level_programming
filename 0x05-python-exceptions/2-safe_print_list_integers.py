#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    c = 0
    i = 0
    try:
        while c < x:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                c += 1
            i += 1
        print()
    except IndexError:
        print()
    return c

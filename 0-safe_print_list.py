#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        cnt = 0
        for i in range(x):
            print(my_list[i], end="")
            cnt += 1
        print()
        return cnt
    except IndexError:
        print()
        return cnt

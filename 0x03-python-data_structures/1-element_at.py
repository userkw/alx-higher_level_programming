#!/usr/bin/python3
def element_at(my_list, idx):
    try:
        result = my_list[idx]
    except IndexError:
        result = None
    return result

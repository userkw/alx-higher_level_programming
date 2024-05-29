#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    nw_l = my_list[:]
    nw_l[idx] = element
    return nw_l

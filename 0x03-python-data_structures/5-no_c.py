#!/usr/bin/python3
def no_c(my_string):
    nw_str = ""
    for char in my_string:
        if char.lower() != "c":
            nw_str += char
    return nw_str

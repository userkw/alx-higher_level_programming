#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l_o = list(a_dictionary.keys())
    l_o.sort()
    for i in l_o:
        print("{}: {}".format(i, a_dictionary.get(i)))

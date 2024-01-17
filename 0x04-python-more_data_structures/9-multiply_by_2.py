#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dir = a_dictionary.copy()
    l_keys = list(n_dir.keys())

    for i in l_keys:
        n_dir[i] *= 2

    return (n_dir)

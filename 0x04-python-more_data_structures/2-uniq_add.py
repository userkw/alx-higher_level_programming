#!/usr/bin/python3
def uniq_add(my_list=[]):
    uq_l = set(my_list)
    nbr = 0

    for a in uq_l:
        nbr += a

    return (nbr)

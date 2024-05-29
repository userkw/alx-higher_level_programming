#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    r = []
    for i in range(list_length):
        d = 0
        try:
            d = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (IndexError, ValueError):
            print("out of range")
        finally:
            r.append(d)
    return r

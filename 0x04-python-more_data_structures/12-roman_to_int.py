#!/usr/bin/python3
def to_subtract(list_num):
    t_s = 0
    m_l = max(list_num)

    for n in list_num:
        if m_l > n:
            t_s += n

    return (m_l - t_s)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(r_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if r_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [r_n.get(ch)]
                else:
                    list_num.append(r_n.get(ch))

                last_rom = r_n.get(ch)

    num += to_subtract(list_num)

    return (num)

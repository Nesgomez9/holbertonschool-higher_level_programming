#!/usr/bin/python3
def roman_to_int(roman_string):
    suma = a = 0
    roman_list = []
    for count in roman_string:
        if count == 'I':
            roman_list.append(1)
        elif count == 'V':
            roman_list.append(5)
        elif count == 'X':
            roman_list.append(10)
        elif count == 'L':
            roman_list.append(50)
        elif count == 'C':
            roman_list.append(100)
        elif count == 'D':
            roman_list.append(500)
        elif count == 'M':
            roman_list.append(1000)
    for i, count in enumerate(roman_list):
        if roman_list[i] > roman_list[i - 1] and i > 0:
            suma += count - (roman_list[i - 1] * 2)
        else:
            suma += count
    return suma

#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        dict_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
        suma = a = 0
        roman_list = []
        for count in roman_string:
            for key in dict_num.keys():
                if count == key:
                    roman_list.append(dict_num[key])
        for i, count in enumerate(roman_list):
            if roman_list[i] > roman_list[i - 1] and i > 0:
                suma += count - (roman_list[i - 1] * 2)
            else:
                suma += count
        return suma
    else:
        return 0

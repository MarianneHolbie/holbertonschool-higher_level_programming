#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0

    # test if string exist or is a string
    if not roman_string or type(roman_string) != str:
        return (0)
    # create dictionary to associate letter and his value
    conversion = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lenght = len(roman_string)

    # special case of only one letter to convert
    if lenght == 1:
        return (conversion.get(roman_string[0]))

    # if minimum 2 letter in string, compare value of letter index and index + 1
    for index in range(0, lenght):
        if index != lenght - 1:
            if conversion.get(roman_string[index]) < conversion.get(roman_string[index + 1]):
                result -= conversion.get(roman_string[index])
            else:
                result += conversion.get(roman_string[index])
        else:
            result += conversion.get(roman_string[index])
    return (result)

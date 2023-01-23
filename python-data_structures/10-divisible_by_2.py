#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_of_two = []
    for i in my_list:
        if i % 2 == 0:
            mul_of_two.append(True)
        else:
            mul_of_two.append(False)
    return (mul_of_two)

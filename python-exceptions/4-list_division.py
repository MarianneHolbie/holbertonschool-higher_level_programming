#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    list_result = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            list_result.append(result)

        # division by 0
        except ZeroDivisionError:
            list_result.append(0)
            print("division by 0")
        # if is not an integer
        except TypeError:
            list_result.append(0)
            print("wrong type")
        # if length give is bigger than the length of both list
        except IndexError:
            list_result.append(0)
            print("out of range")

        finally:
            pass

    return (list_result)

#!usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            elif not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                raise TypeError
            elif my_list_2[i] == 0:
                raise ZeroDivisionError
            else:
                result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(0)
    return result

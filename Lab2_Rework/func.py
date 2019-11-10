import re

def is_integer(start_str):
    return bool(re.match(r"^[+-]?\d+$", start_str))

def int_Validator(prop_str=""):
    temp_int = input(prop_str)
    while not is_integer(temp_int):
        temp_int = input(prop_str)
    return int(temp_int)

def is_float(start_str):
    return bool(re.match(r"^[+-]?\d+\.?\d*$", start_str))

def float_Validator(prop_str=""):
    temp_float = input(prop_str)
    while not is_float(temp_float):
        temp_float = input(prop_str)
    return float(temp_float)

def setChoice():
    print("Ви би хотіли розпочати знову?\n1) так\n2) ні")
    i = 1
    j = 1
    while i == 1:
        c = int_Validator()
        if c == 1:
            print("Починаэмо спочатку")
            i += 1
        elif c == 2:
            print("До побачення")
            i += 1
            j += 1
        else:
            print("У вас є можливість обрати лише з 2 пунктів")
    return j

def welcome(a):
    print("Лабораторна робота №%d Майструк Ілля №6\nДоброго дня" %(a))
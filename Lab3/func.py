import re

def is_one_symbol(start_str):
    return bool(re.match(r"^\S$", start_str))

def is_integer(start_str):
    return bool(re.match(r"^[+-]?\d+$", start_str))

def is_negative_integer(start_str):
    return bool(re.match(r"^[-]?\d+$", start_str))

def is_positive_integer(start_str):
    return bool(re.match(r"^[+]?\d+$", start_str))

def is_float(start_str):
    return bool(re.match(r"^[+-]?\d+\.?\d*$", start_str))

def int_Validator(prop_str="", type_of=""):
    temp_int = input(prop_str)
    if type_of == "+":
        while not is_positive_integer(temp_int):
            temp_int = input("Введіть ціле додатнє число: ")
    elif type_of == "-":
        while not is_negative_integer(temp_int):
            temp_int = input("Введіть ціле від'ємне число: ")
    else:
        while not is_integer(temp_int):
            temp_int = input("Введіть ціле число: ")
    return int(temp_int)

def one_symbol(prop_str=""):
    temp_symbol = input(prop_str)
    while not is_one_symbol(temp_symbol):
        temp_symbol = input("Введіть один символ: ")
    return temp_symbol

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

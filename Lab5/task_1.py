import func
import keyboard

def execute():
    first_list = []
    second_list = []
    result_list = []
    first_len = func.int_Validator("Введіть розмір першого списку:")
    second_len = func.int_Validator("Введіть розмір другого списку:")
    for i in range(first_len):
        first_list.append(func.int_Validator("Введіть " + str(i+1) +" число першого списку:"))
    for i in range(second_len):
        second_list.append(func.int_Validator("Введіть " + str(i+1) +" число другого списку:"))
    first_list.sort()
    second_list.sort()
    print("Перший перелік: ", first_list)
    print("Другий перелік: ", second_list)
    for el_1 in first_list:
        for el_2 in second_list:
            if el_1 == el_2:
                result_list.append(el_1)
    print("Перелік загальних елементів: ", result_list)
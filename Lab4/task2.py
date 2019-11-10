import func

def Delete(local_str, start, lenght):
    result = local_str[:start-1] + local_str[start+lenght-1::]
    return result

def execute():
    rand_str = "abcdefghijklmnopqrstuvwxyz"
    start = -1
    lenght = -1
    print(rand_str)
    max_len = len(rand_str)
    print("Введіть початковий індекс:")  # input int(0:len)
    while start < 1 or start>max_len-1:
        start = func.checkType("int")
        if start < 1 or start>max_len-1:
            print("Введіть число (1 до 25): ")
    print("Введіть довжину слайсу:")
    while lenght < 0:
        lenght = func.checkType("int")
        if lenght < 0:
            print("Введіть число від 0: ")
    res_str = Delete(rand_str, start, lenght)
    print(res_str)

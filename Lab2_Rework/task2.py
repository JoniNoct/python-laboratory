import func

def execute():
    print("Введіть число n:")
    i = 1
    while i == 1:
        varN = func.int_Validator()
        if varN < 1:
            print("Введіть значення більше 1")
        else:
            i += 1
    j = 1
    while j <= varN:
        print(j ** 2)
        j += 1
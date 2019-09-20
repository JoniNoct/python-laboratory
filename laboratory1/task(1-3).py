def checkType(a):
    i = 1
    if a == "int":
        while i == 1:
            try:
                v = int(input())
                i += 1
            except:
                print("Потрібно ввести число")
        return v
    elif a == "float":
        while i == 1:
            try:
                v = float(input())
                i += 1
            except:
                print("Потрібно ввести число")
        return v

def setChoice():
    print("Ви би хотіли розпочати знову?\n1) так\n2) ні")
    i = 1
    j = 1
    while i == 1:
        c = checkType("int")
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

i = 1
print("Доброго дня")  # entering
while i == 1:
    print("Будь ласка оберіть номер завдання:\n1) Температура\n2) Числа\n3) Функція\n4) Вихід")
    taskNumber = checkType("int")

    if taskNumber == 1:  # temp
        print("Введіть кількість градусів Цельсія:")
        tempCelsius = checkType("float")
        tempFahrenheit = (tempCelsius * (9 / 5)) + 32
        print(tempCelsius, "градусів Цельсія = ", tempFahrenheit, "градусів Фаренгейта")
        i = setChoice()

    elif taskNumber == 2:  # variables refactor
        print("Введіть число a:")
        varA = checkType("int")
        print("Введіть число b:")
        varB = checkType("int")
        if varA == varB:
            varA = 0
            varB = 0
            print(varA, varB)
        elif varA > varB:
            varB = varA
            print(varA, varB)
        else:
            varA = varB
            print(varA, varB)
        i = setChoice()

    elif taskNumber == 3:  # function
        print("Введіть змінну x:")
        varX = checkType("float")
        if varX > 7:
            print("F(x) = ", 1/(varX**2-4))  # ділення на 0 не відбувається, бо х > 7
        else:
            print("F(x) = ", 3*varX-9)
        i = setChoice()

    elif taskNumber == 4:  # exit
        print("До побачення")
        i += 1

    else:  # limited variants
        print("У вас є можливість обрати лише з 4 пунктів")
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

def welcome(a):
    print("Лабораторна робота №%d Майструк Ілля №6\nДоброго дня" %(a))

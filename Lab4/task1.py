import func

def calculator(X, Y, act):  # calculator
    if act == 1:
        return X+Y
    elif act == 2:
        return X-Y
    elif act == 3:
        return X*Y
    elif act == 4:
        if Y==0:
            print("Ділення на ноль.")
        else:
            return X/Y

def execute():
    varX = -1
    varY = -1
    print("Введіть дійсне додатнє число X:")  # input float+
    while varX < 0:
        varX = func.checkType("float")
        if varX < 0:
            print("Введіть додатнє число: ")
    print("Введіть дійсне додатнє число Y:")
    while varY < 0:
        varY = func.checkType("float")
        if varY < 0:
            print("Введіть додатнє число: ")
    print("Оберіть дію над числами:\n1) Додавання\n2) Віднімання\n3) Множення\n4) Ділення")  # choose action
    action = 0
    while action < 1 or action > 4:
        action = func.checkType("int")
        if action < 1 and action > 4:
            print("Оберіть дію з 1-4: ")
    result = calculator(varX, varY, action)  # result

    print("Результат: ", result)  # output result data
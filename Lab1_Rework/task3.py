import func

def execute():
    print("Введіть змінну x:")
    varX = func.float_Validator()
    if varX > 7:
        print("F(x) = ", 1 / (varX ** 2 - 4))  # ділення на 0 не відбувається, бо х > 7
    else:
        print("F(x) = ", 3 * varX - 9)
import func

"""
Обчислення конкретної функції, в залежності від введеного значення х
F(x) = 3x-9, якщо x <=7 | та 1/(x**2-4), якщо x > 7
"""

def execute():
    print("Введіть змінну x:")
    varX = func.float_Validator()
    if varX > 7:
        print("F(x) = ", 1 / (varX ** 2 - 4))  # ділення на 0 не відбувається, бо х > 7
    else:
        print("F(x) = ", 3 * varX - 9)

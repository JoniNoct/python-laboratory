import func

"""
Обчислити суму (x-i)/(i**2) для перших n членів починаючи з 1.
"""

def execute():
    print("Введіть число x:")
    varX = func.float_Validator()
    print("Введіть число n:")
    i = 1
    while i == 1:
        varN = func.int_Validator()
        if varN < 1:
            print("Введіть значення більше 1")
        else:
            i += 1
    sum = 0.0
    for j in range(1, varN+1):
        sum += (varX-j)/j**2
    print("Сумма: ",sum)

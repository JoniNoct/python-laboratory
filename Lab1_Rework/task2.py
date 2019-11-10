import func

def execute():
    print("Введіть число a:")
    varA = func.int_Validator()
    print("Введіть число b:")
    varB = func.int_Validator()
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

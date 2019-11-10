import func

def execute():
    print("Введіть кількість градусів Цельсія:")
    tempCelsius = func.float_Validator()
    tempFahrenheit = (tempCelsius * (9 / 5)) + 32
    print(tempCelsius, "градусів Цельсія = ", tempFahrenheit, "градусів Фаренгейта")
import func

"""
Дано значення температури в градусах Цельсія. Вивести температуру в градусах Фаренгейта.
"""

def execute():
    print("Введіть кількість градусів Цельсія:")
    tempCelsius = func.float_Validator()
    tempFahrenheit = (tempCelsius * (9 / 5)) + 32
    print("{0} градусів Цельсія = {1} градусів Фаренгейта".format(tempCelsius, tempFahrenheit))

import func

"""
Доповнити символом '*' слова, що мають довжину менше заданої (максимальної) до максимальної.
"""

func.welcome(3)  # entering
i = 1
while i == 1:
    custom_symbol = func.one_symbol("Введіть один символ для доповнення: ")
    print("Введіть довжину слова: ", end="")
    max_char = func.int_Validator(type_of="+")
    print("Ви бажаэте вводити строку? \n1) Так\n2) Ні(заповнити її Lorem ipsum gen)")
    text_input_choice = 0
    while text_input_choice < 1 or text_input_choice > 2:
        text_input_choice = func.int_Validator(type_of="+")
    if text_input_choice == 2:
        text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    else:
        text = input("Введіть звичайний текст: ")
    text_words = text.split()
    index = 0
    for el in text_words:
        while len(el) < max_char:
            el += custom_symbol
        text_words[index] = el
        index += 1
    text_result = " ".join(text_words)
    print(text_result)
    i = func.setChoice()

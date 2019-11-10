import func

func.welcome(3)  # entering
i = 1
while i == 1:
    max_char = -1
    print("Введіть довжину слова: ")
    while max_char < 0:
        max_char = func.checkType("int")
        if max_char < 0:
            print("Введіть довжину, більшу за 0")

    text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    text_words = text.split()
    index = 0
    for el in text_words:
        while len(el) < max_char:
            el += "*"
        text_words[index] = el
        index += 1

    text_result = " ".join(text_words)
    print(text_result)
    i = func.setChoice()
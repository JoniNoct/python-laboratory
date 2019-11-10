import func
import task1 as t1
import task2 as t2
import task3 as t3

func.welcome(1)  # entering
i = 1
while i == 1:
    print("Будь ласка оберіть номер завдання:\n1) Конвертація у градуси Фаренгейта\n2) Обробка двох значень\n3) Обчислення функції\n4) Вихід")
    taskNumber = func.int_Validator()

    if taskNumber == 1:  # temp
        t1.execute()
        i = func.setChoice()

    elif taskNumber == 2:  # variables refactor
        t2.execute()
        i = func.setChoice()

    elif taskNumber == 3:  # function
        t3.execute()
        i = func.setChoice()

    elif taskNumber == 4:  # exit
        print("До побачення")
        i += 1

    else:  # limited variants
        print("У вас є можливість обрати лише з 4 пунктів")
import func
import task_1 as t1
import task_2 as t2

func.welcome(5)  # entering
i = 1
while i == 1:
    print("Будь ласка оберіть номер завдання:\n1) Списки\n2) Множини\n3) Вихід")
    taskNumber = func.int_Validator()

    if taskNumber == 1:  # for
        t1.execute()
        i = func.setChoice()

    elif taskNumber == 2:  # while
        t2.execute()
        i = func.setChoice()

    elif taskNumber == 3:  # exit
        print("До побачення")
        i += 1

    else:  # limited variants
        print("У вас є можливість обрати лише з 3 пунктів")
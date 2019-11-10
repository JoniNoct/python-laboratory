import func
import task1 as t1
import task2 as t2
func.welcome(4)  # entering
i = 1
while i == 1:
    print("Будь ласка оберіть номер завдання:\n1) Функції на обчислення і логіку\n2) Функції для роботи з рядками\n3) Вихід")
    taskNumber = func.checkType("int")

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
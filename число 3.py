import time
prod = 0
while prod == 0:
    try:
        Rep = True
        while Rep == True:
            num = int(input("Число 3-магическое. Давай докажу) Введи абсолютно любое число: "))
            print("Умножим его на два. Получится ", num * 2)
            time.sleep(3)
            print("Прибавим к этому числу 6 и получим ", num * 2 + 6)
            time.sleep(3)
            print("Разделим результат на два, получив ", (num * 2 + 6) / 2)
            time.sleep(3)
            print("Вычитаем задуманное число и получаем ", (num * 2 + 6) / 2 - num)
            time.sleep(3)
            print("Получилось число 3.")
            Rep = input("Повторим?(Да/Нет) ")
            if Rep == "Да" or Rep == "да":
                Rep = True
            elif Rep == "Нет" or Rep == "нет":
                Rep = False
                prod += 1
            else:
                print("Я тебя не понимаю!")
                Rep = True
        while Rep == False:
            print("Жалко, что ты уходишь. До встречи!")
            break
    except ValueError:
        print("Введите лучше число")


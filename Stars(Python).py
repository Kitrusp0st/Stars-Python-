for i in range(10):


    PressF = input("Задача 1, Задача 2, Задача 3")

    if PressF == "1":
        print(" ")
        print(" ")
        print("Задача 1 (Треугольник из звёздочек)")
        print(" ")
        for i in range(1, 6): print('*' * i)



    elif PressF == "2":
        print(" ")
        print(" ")
        print("Задача 2 (Имя в рамке из звёздочек)")
        print(" ")
        name = input("Введите имя: ")
        print({'*' * (len(name) + 2)})
        print({name})
        print({'*' * (len(name) + 2)})


    elif PressF == "3":
        print(" ")
        print(" ")
        print("Задача 3 (Сумма чисел от 1 до n)")
        print(" ")
        n = int(input("Введите число n: "))
        print(sum(range(1, n + 1)))
    print(f"Попытки закончились. Было загадано число {secret_number}")

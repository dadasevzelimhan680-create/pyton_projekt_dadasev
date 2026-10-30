#

while True:
    try:
        a = int(input("Введите целое число:"))
        b = int(input("Введите целое число:"))
        if a <= 0 or b <=0:
            print("Ошибка: Длины отрезков должны быть больше 0 :")
        elif a <= b:
            print("Ошибка: Отрезок А должен быть больше B:")
        else:
            break
    except ValueError:
        print("Неправильно ввели!,введите целое число:")
otvet = a % b
print("Длина незанятой части отрезка A:", otvet)

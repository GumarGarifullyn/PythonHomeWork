import math
sum = int(input("Введите сумму двух числе x и y: "))
mult = int(input("Введите произведение двух числе x и y: "))
disc = sum**2 - 4*mult
if disc < 0:
    print("Невозможно подобрать x и y для заданных вами параметров")
elif disc > 0:
    print("Возможны 2 варианта решения:", end = " ")
    x = (sum + math.sqrt(disc))/2*mult
    y = sum - x
    print(x, y, end = " ")
    x = (sum - math.sqrt(disc))/2*mult
    y = sum - x
    print(x, y)
else:
    print("Возможен лишь 1 вариант решения:", end = " ")
    x = (sum - math.sqrt(disc))/2*mult
    y = sum - x
    print(x, y)
    
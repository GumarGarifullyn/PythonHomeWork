# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math
sum = int(input("Введите сумму двух числе x и y: "))
mult = int(input("Введите произведение двух числе x и y: "))
disc = sum**2 - 4*mult
print(sum, mult, disc)
if disc < 0:
    print("Невозможно подобрать x и y для заданных вами параметров")
elif disc > 0:
    print("Возможны 2 варианта решения:", end = " ")
    x = (sum + float(math.sqrt(disc)))/2*mult
    y = sum - x
    print("x1 =",round(float(x),3), "y1 =", round(float(y),3), end = " или ")
    x = (sum - float(math.sqrt(disc)))/2*mult
    y = sum - x
    print("x2 =",round(float(x),3), "y2 =", round(float(y),3))
else:
    print("Возможен лишь 1 вариант решения:", end = " ")
    x = (sum - float(math.sqrt(disc)))/2*mult
    y = sum - x
    print("x =",round(float(x),3), "y =", round(float(y),3))

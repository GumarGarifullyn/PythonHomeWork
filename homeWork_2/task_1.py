# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
lst = []
n = int(input('Введите сколько раз нужно подбросить монету: '))
zero = 0
one = 0
for i in range(int(n)):
    lst.append(randint(0,1))
    if lst[i] == 0:
        zero += 1
    else: 
        one += 1
print(lst)
if zero > one:
    print("Минимальное количество монет, которые нужно перевернуть", n-zero)
else:
    print("Минимальное количество монет, которые нужно перевернуть", n-one)

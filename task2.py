# В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

room1 = int(input("Введите количество учащихся в первом классе: "))
room2 = int(input("Введите количество учащихся во втором классе: "))
room3 = int(input("Введите количество учащихся в третьем классе: "))
print(f"Для 3 классов нужно {(room1+1)//2+(room2+1)//2+(room3+1)//2} парт(ы)")
#  За день машина проезжает n километров. Сколько дней нужно,
#  чтобы проехать маршрут длиной m километров?
#  При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# **Input:**
# n = 700
# m = 750
# **Output:**

n = 700
m = int(input("Введите количество км, которые нужно проехать: "))
print(int((m+n-1)/n))


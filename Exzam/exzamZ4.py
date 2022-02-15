# Посчитать, сколько раз встречаутся определенная цифра в числах.
# Количество введенынх  и искомая цифра задаются с клавиатуры.
# Числа выбираются рандомно.
import random
n = int(input("Ввелите колличество чисел : "))
n2 = int(input("Введите искомая цифра : "))
m = []
c = 0
for i in range(0, n):
    n3 = random.randint(1, 1000)
    m.append(n3)
print(m)
for i1 in m:
    i = str(i)
    for j in i:
        j = int(j)
        if n2 == j:
            c += 1
        print(c)

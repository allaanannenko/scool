# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
i1 = 0
i2 = 0
a = 0
b = 0
h = 0
list = [15, 48, 'hello', 6, 19, 'world']
print("Дан список", list)
for i in list:
    if type(i) == int and i % 2 == 0:
        i1 = i // 10
        i2 = i % 10
        s = i1 + i2
        print("Четное число из списка-", i, "Сумма цифр четного числа = ", s)
    if type(i) == int and i % 2 != 0:
        a = list.index(i)
        list[a] = 1
    if type(i) == str:
        for c in i:
            if c.lower() in "aeiou":
                h += 1
            else:
                b += 1
print("Гласных = ", h, "Согласных = ", b)
print("Нечетные числа заменили на 1 - ", list)



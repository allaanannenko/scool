# Массив из 7 цифр. Если четных цифр в нем больше чем нечетных,
# то найти сумму всех его цифр, если нечетных больше,
# то найти произведение 1 3 и 6 элемента.

mas = [3, 4, 6, 1, 7, 9, 2]
a = 0
d = 0
for i in mas:
    if i % 2 == 0:
        a += 1
    else:
        d += 1

if a > d:
    a += i
    print("Сумма четных чисел : ", a)
else:
    print(mas[1] * mas[3] * mas[6])



#Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.

mas = [25, 0, 25, 4, 6, 0, 6, 1, 7, 15, 0]
mas2 = []
for i in mas:
    if mas.count(i) >= 2:
        mas2.append(i)
        print(mas2)

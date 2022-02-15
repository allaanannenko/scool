#Записать в массив все числа в диапазоне от 1 до 500 кратные 5.
f = []
for i in range(1, 500):
    if i % 5 == 0:
       f.append(i)
       print(list(i))


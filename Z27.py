# Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.
import json
mas = ['Hello', 12, 'World', 4, 'Day', 10, 'Python', 7]
s = []
a = []
for i in mas:
    if type(i) is str:
        s.append(i)
        s.sort()
    if type(i) is int:
        a.append(i)
        a.sort()
    d = s + a
with open('my_mas.txt', 'w') as file:
    file.write(str(d))
with open('my_mas.txt', 'r' ) as file:
    c = file.readlines()
    print(c)


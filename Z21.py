# Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

str = 'pythonist'
for i in str:
    my_dict = {i: str.count(i) for i in str}
print(my_dict)
# Сформировать из введенного числа обратное
# по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

a = int(input())
n = 0
while a > 0:
    n = n * 10 + a % 10
    print(n)
    a = a // 10
print(n)









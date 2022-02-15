s1 = input("Строка : ")
s2 = input("Буква : ")
c =""
for i in s1:
    if i != s2:
        c += i
    print("результат :", c)
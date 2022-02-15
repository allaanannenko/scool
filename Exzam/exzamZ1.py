a = int(input("Введите семизначное число : "))
b = str(a)
even = 0
odd = 0
for i in b:
    c = int(i)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if even < odd:
    even += i
    print("Сумма всех всех четных цифр = ", even)
else:
    print(b[1] * b[3] * b[6])


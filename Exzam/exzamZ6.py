# Посчитать сколько пар (стоят рядом) верхнего и нижнего регистра находятся
# в веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего),
# а также сколько всего букв в слове, сколько гласных и согласных.
text = str(input("Введите строку с разным регистром : "))
p1 = ""
p2 = ""
a1 = 0
a2 = 0
for a in text:
    if a.islower():
        p1 += a
        if len(p1) == 2 and len(p1) % 2 == 0:
            a1 += 1
        elif p1 != "":
            p1 = ""
    if a.isupper():
        p2 +=  a
        if len(p1) == 2 and len(p1) % 2 == 0:
            a2 += 1
        elif p2 != "":
            p2 = ""
print(a1, "пары верхнего регистра")
print(a2, "пары нижнего регистра")
len = len(text)
print("В слове", len, "букв")
vowels = 0
consonants = 0
for i in text:
    if i.lower() in 'aeiouy':
        vowels += 1
    else:
        consonants += 1
print("Гласных букв", vowels)
print("Согласных букв", consonants)

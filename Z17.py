# Найти самое длинное слово в строке.

string = input("Введите строку : ")
string_split = string.split()
string2 = []
for i in range(len(string_split)):
    a = len(string_split[i])
    string2.append(int(a))

print(string_split[(string2.index((max(string2))))])










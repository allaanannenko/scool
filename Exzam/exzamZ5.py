# Вводится строка, содержащая буквы, целые числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран.
# Строка может содержать пробелы.
string = input("Введите строку содержащую буквы и цифры : ")
l = ""
for i in string:
    if i.isdigit():
        l += i
    elif l != "":
        print(l)
        l = ""
if l != "":
    print(l)









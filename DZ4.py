# Напишите программу , которая просит ввести любую букву из алфавита.
# После чего выводит порядковый номер который занимает буква. И наоборот.

str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

a = input("Введите букву алфавита/порядковый номер буквы:")

if a in str:
   print("Номер введенной Вами буквы в алфавите:", str.find(a)+1)
if a.isdigit():
    b = int(a)
    b = b-1
    print("Буква алфавита согласно введенного Вами номера", str[b])










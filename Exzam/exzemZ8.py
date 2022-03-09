# Задача 2:
# Напишите программы создания файла добавления в него записей,
# удаления записей, исправления записей, вывода содержимого файла на экран
# (все описать в функциях)
# ------------------------залить все это на github и скинуть мне ссылки.
import os
with open("text.txt", "w", encoding='utf-8') as f:
    f.write("This is text files!")
with open("text.txt", "r", encoding='utf-8') as f:
    print(f.readline())
with open("text.txt", "a", encoding='utf-8') as f:
    f.write("This is text files 2 !")
with open("text.txt", "r", encoding='utf-8') as f:
    print(f.readline())




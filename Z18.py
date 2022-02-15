# Преобразовать текст в список слов с удалением знаков препинания.
txt = input("Введите текст: ")
txt2 = ""
punct = '''"/?!@;#$%^*()_-,.><[]{}'''
for i in txt:
    if i not in punct:
        txt2 = txt2 + i
l = list(txt2.split())
print(l)


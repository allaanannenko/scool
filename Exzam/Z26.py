with open('article.txt', 'w', encoding='utf-8') as f:
    f.write("""Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела""")
with open('article.txt', 'r', encoding='utf-8') as f:
    d = f.readlines()
    print(d)
    s = []
    for i in d:
        a = len(i)
        s.append(a)
        b = s.index(max(s))
print(d[b])




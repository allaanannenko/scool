# Дан список. Выведите те его элементы,
# которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.
# спискеa = [1, 2, 3, 3, 4, 5, 6, 6]
# b = []
# for i in a:
#     if a.count(i) < 2:
#         b.append(i)
# print(b)

# a = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6]
# b = []
# for i in a:
#     if a.count(i) == 2:
#         b.append(i)
# print(len(b) // 2)
# print(b)
# Преобразовать текст в список слов с удалением знаков препинания.
# Например: python, JS! C? преобразуется в python JS C
# a = "python, JS! C?"
# z = [",", "!", "?",]
# b = ""
# for i in a:
#     if i not in z:
#         b += i
# d =
# Клиент приходит в кондитерскую.  Он хочет приобрести один или несколько видов продукции,
# а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
# Предложите выбор:
#
# Если человек хочет посмотреть описание: название – описание
# Если человек хочет посмотреть цену: название – цена.
# Если человек хочет посмотреть количество: название – количество.
# Всю информацию.
# Приступить к покупке:
# 	С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# 	Посчитать цену выбранных товаров и сколько товаров осталось в изначальном 	списке
# До свидания

# a = input("введите название торта (n – выход из программы) :")
# b = int(input("Ведите кол-во(n-выход из программы) : "))
# c = []
# while True:
#     if a == 'n' and b == 'n':
#         break
#     else:
#         for i in a:
#             if i ==

# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу
nums = []
with open("data.txt", 'w',encoding='utf-8') as f:
    f.write("Петров Николай 10\nСидоров Сергей 3\nКирильчик Светлана 2 ")
with open("data.txt", "r", encoding='utf-8') as f1:
    f = f1.read()

# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
def operation_plus(a, b):
    return a + b
def operation_minus(a, b):
    return a - b
def operation_proizvedenie(a, b):
    return a * b
def operation_delenie(a, b):
    return a / b

while True:
    oper = input('Введите знак операции (+,-,*,/): ')
    if oper == '0':
        break
    if oper in ('+', '-', '*', '/'):
        x = float(input('Введите 1-е число x = '))
        y = float(input('Введите 2-е число y = '))
    if oper == '+':
        print(x, '+', y, '=', operation_plus(x, y))
    elif oper == '-':
        print(x, '-', y, '=', operation_minus(x, y))
    elif oper == '*':
        print(x, '*', y, '=', operation_proizvedenie(x, y))
    elif oper == '/':
        if y != 0:
            print(x, '/', y, '=',  operation_delenie(x, y))
        else:
            print('Деление на ноль.')
    else:
        print('Вы ввели неверный знак операции!')
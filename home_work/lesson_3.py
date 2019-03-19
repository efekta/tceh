# **Задачи на обработку ошибок:
# 1. Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, 
# если оно меньше 0 - TypeError, если оно больше 10 - IndexError. 
# Обрабатываем ошибку, говорим пользователю, в чем его ошибка
# try:
#     user_input = int(input('Введите число: '))
#     if user_input % 2 == 0 and user_input < 10:
#         raise ValueError('Это число четное!')
#     if user_input < 0:
#         raise TypeError('Это число меньше нуля!')
#     if user_input > 10:
#         raise IndexError('Это число больше 10!')
# except ValueError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# 2. Создайте список произвольной длины.
# Пользователь должен ввести индекс объекта, который хочет посмотреть.
# Если все хорошо - пишите объект в консоль.
# Если нет - обработайте возмозможные ошибки и скажите ему, что не так

# l = ['5', 'Liliya', 'hi!']
# try:
#     user_input = int(input('Введи индекс объекта, который хочешь посмотреть: '))
#     if user_input >= 0:
#         if user_input >= len(l):
#             raise IndexError('Нет такого индекса!')
#     print(l[user_input])
# except IndexError:
#     print('Нет такого индекса!')
# except ValueError:
#     print('Некорректный ввод индекса!')






# **Задачи на закрепление функций:
# 1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля,
# возвращаем их сумму
# Если оба меньше - разность. Если знаки разные - возвращаем 0
# x = int(input('Введи число: '))
# y = int(input('Введи еще одно число: '))
# def args(x,y):
#     if x > 0 and y > 0:
#         return print(x + y)
#     if x < 0 and y < 0:
#         print(x - y)
#     else:
#         print(0)
# args(x,y)

# 2.Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль
a = int(input('введи число: '))
b = int(input('введи еще число: '))
c = int(input('введи еще одно число: '))
l = [a, b, c]

def f(seq):
    m1 = m2 = None
    for i in seq:
        if m2 is None:
            m2 = i
        elif m1 is None:
            if i > m2:
                m1, m2 = m2, i
            else:
                m1 = i
        elif i > m2:
            m1, m2 = m2, i
        elif i > m1:
            m1 = i
    print(m1, m2)
f(l)

# 3.Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. 
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, 
# если флаг отрицателен - возвращаем новый список с четными числами из входного списка

# **Задачи на закрепление типов аргументов:
# 1.Написать функцию, которая принимает любое количество аргументов чисел. 
# Среди них она находит максимальное и минимальное. И возвращает оба

# 2.Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. 
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, 
# иначе - к нижнему

# 3.Написать функцию, которая принимает любое количество позиционных 
# аргументов - строк и один парматер по-умолчанию glue, который равен ':'. 
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. 
# Для соединения между любых двух строк вставлять glue

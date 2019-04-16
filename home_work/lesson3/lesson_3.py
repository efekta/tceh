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
# a = int(input('введи число: '))
# b = int(input('введи еще число: '))
# c = int(input('введи еще одно число: '))
# l = [a, b, c]
#
# def f(seq):
#     m1 = m2 = None
#     for i in seq:
#         if m2 is None:
#             m2 = i
#         elif m1 is None:
#             if i > m2:
#                 m1, m2 = m2, i
#             else:
#                 m1 = i
#         elif i > m2:
#             m1, m2 = m2, i
#         elif i > m1:
#             m1 = i
#     print(m1, m2)
# f(l)
# or
# def function(x,y,z):
#     lst = [x,y,z]
#     lst.sort()
#     print(lst[1],lst[2])
# function(8,5,10)
# 3.Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. 
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, 
# если флаг отрицателен - возвращаем новый список с четными числами из входного списка
# arg_list = [25, 76, 89, 66, 12, 0, 454, 33]
# bool_list = True
# num_list = []
# def func(*arg_list, bool_list):
#     if bool_list == True:
#         for x in arg_list:
#             if x % 2 == 0 and x != 0:
#                 num_list.append(x)
#         print(num_list)
#     elif bool_list == False:
#         for x in arg_list:
#             if x % 2 != 0:
#                 num_list.append(x)
#         print(num_list)
# func(arg_list, bool_list)
# or
# def function(*numbers,flag):
#     if flag:
#         return list_num1
#         print(function)
#     else:
#         return list_num2
#     print(function)
#
#
# def function1(*numbers,flag):
#     list_num1 = []
#     if flag==False:
#         for number in numbers:
#             if number % 2 == 0:
#                 list_num1.append(number)
#     return list_num1
#
# def function2(*numbers,flag):
#     list_num2 = []
#     if flag==True:
#         for number1 in numbers:
#             if number1 % 2 != 0:
#                 list_num2.append(number1)
#     return list_num2
# **Задачи на закрепление типов аргументов:
# 1.Написать функцию, которая принимает любое количество аргументов чисел. 
# Среди них она находит максимальное и минимальное. И возвращает оба
# def f(*x):
#     my = []
#     my.append(min(x))
#     my.append(max(x))
#     return my
#
# print(f(55, 790, 43, 0, 12))

# 2.Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. 
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, 
# иначе - к нижнему
# def args(s, case = True):
#     if case:
#         return s.upper()
#     else:
#         return s.lower()
# print(args('LLilyYa', ''))

# 3.Написать функцию, которая принимает любое количество позиционных 
# аргументов - строк и один парматер по-умолчанию glue, который равен ':'. 
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. 
# Для соединения между любых двух строк вставлять glue

# def f(*s, glue=':'):
#     l = []
#     for i in s:
#         if len(i) > 3:
#             l.append(i)
#     return glue.join(l)
# print(f('tratata','no','fine','yeas'))

'''
Напишите функцию, которая принимает число в качестве
ввода, возводит его в квадрат и возвращает.
'''
# так
def f() :
	num = input('Введите число: ')
	num = int(num)
	return num * 2
print(f())

f()
# или так
def squared(x):
    return x ** 2

print(squared(2))

'''
Создайте функцию, которая принимает строку в качестве параметра
и возвращает ее.
'''
# так
def f_str():
	my_str = input('Введите строку: ')
	print(my_str)

f_str()
# или так
def print_string(string):
    print(string)

print_string("Проверка: 1, 2, 3.")
'''
Напишите функцию, которая принимает 
3 обязательных и 2 необязательных
параметра.
'''
def main_f(x, q, w, y = 2, z = 4):
	return x + q - w + y + z
result = main_f(1, 2, 3)
print(result)
# main_f()

'''
Напишите программу с 2-мя функциями. Первая должна принимать в качестве параметра
целое число и возвращать результат деления этого числа на 2.

Вторая функция должна принимать в качестве параметра целое число и
возвращать результат умножения этого числа на 4.

Вызовите первую функцию, сохраните результат в переменной и передайте ее
в качестве параметра во вторую функцию.
'''
# так
number_in = input('Введите число: ')
number_in = int(number_in)
def first_func ():
    return number_in // 2
first_result = first_func()
print(first_result)

def tw_func (first_result = first_func()):
	return first_result * 4
tw_result = tw_func()
print(tw_result)
# или так
def divide(x):
    return x / 2


def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)

print(z)
'''
Напишите функцию, которая преобразовывает строку в тип данных float
и возвращает результат.
Используйте обработку исключений, что бы перехватить возможные исключения.
'''
# c = input('Введите число: ')
def convert(string):
    try:
        return float(string)
    except ValueError:
        print('Не удалось преобразовать строку в число с плавающей точкой.')

c = convert('55')
print(c)
# Простые задачки (для новичков, необязательно для выполнения):

# Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон
a = int(input('Введите длинну первой сторны прямоугольника: '))
b = int(input('Введите длинну второй сторны прямоугольника: '))
s = print(a * b)

# ########################################################
# Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-".
# В зависимости от знака выводит их сумму или разницу
def func_numbers():
	a = int(input('Введите число: '))
	b = int(input('Введите еще одно число: '))
	result = input('Введите знак арифметического действия + или - : ')
	if result == '+':
		amount = a + b
		print(amount)
	elif result == '-':
		difference = a - b
		print(difference)
func_numbers()

# ###############################################
# Напишите программу, которая находит все простые числа между 0 и пользовательским числом
# Просто́е число́ (др.-греч. πρώτος ἀριθμός) — натуральное (целое положительное) число,
# имеющее ровно два различных натуральных делителя — единицу и самого себя.

# Решето Эратосфена:
n = int(input('Введите число: '))
 
# список заполняется значениями от 0 до n
a = []
for i in range(n + 1):
    a.append(i)
 
# Вторым элементом является единица,
# которую не считают простым числом
# забиваем ее нулем.
a[1] = 0
 
# начинаем с 3-го элемента
i = 2
while i <= n:
    # Если значение ячейки до этого не было обнулено,
    # в этой ячейке содержится простое число.
    if a[i] != 0:
        # первое кратное ему будет в два раза больше
        j = i + i
        while j <= n:
            # это число составное, поэтому заменяем его нулем
            a[j] = 0
            # переходим к следующему числу, которое кратно i (оно на i больше)
            j = j + i
    i += 1
 
# Превращая список во множество, 
# избавляемся от всех нулей кроме одного.
a = set(a)
# удаляем ноль
a.remove(0)
print(a)




# Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами
num_1 = int(input('Введите число: '))
num_2 = int(input('Введите еще число: '))
list = []
my_lst = []
if num_1 >= num_2:
	print('Первое число должно быть меньше, чем второе!')
for item in range(num_1, num_2 + 1):
	list.append(item)
for i in list:
	if i % 5 == 0:
		my_lst.append(i)

# or:

while True:
	num_1 = int(input('Введите число: '))
	num_2 = int(input('Введите еще число: '))
	list = []
	my_list = []
	if num_1 >= num_2:
		print('Первое число должно быть меньше, чем второе!') continue
	else:
		for item in range(num_1, num_2 + 1):
			list.append(item)
		for i in list:
			if i % 5 == 0:
				my_list.append(i)
print(my_list)






















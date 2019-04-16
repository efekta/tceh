#Написать функцию, которая выбрасывает одно из трех исключений:
#TypeError, RuntimeError, ValueError случайным образом.
#В месте вызова функции обрабатывать все три исключения.

def er ():
    import random
    number=random.randint(0,2)
    if number == 0:
        try:
            raise TypeError()
        except TypeError:
            print ('random_number_is_0!!!')
    elif number == 1:
        try:
            raise ValueError()
        except ValueError:
            print ('random_number_is_1!!!')
    else:
        try:
            raise RuntimeError()
        except RuntimeError:
            print ('random_number_is_2!!!')
er()

# or

def er ():
	number = int(input('Введи число: '))
	if number == 0:
	    try:
	        raise TypeError()
	    except TypeError:
	        print ('Ты ввел ' + str(number))
	elif number == 1:
	    try:
	        raise ValueError()
	    except ValueError:
	        print ('Ты ввел ' + str(number))
	else:
	    try:
	        raise RuntimeError()
	    except RuntimeError:
	        print('Ты ввел ' + str(number))
er()

# and or
def error_func():
  import random
  number = random.randint(0,10)
  if number == 0:
    try:
      raise ValueError
    except ValueError:
      print('This number 0!')
  elif number > 0 and number < 10 and number != 0:
    try:
      raise TypeError
    except TypeError:
      print('This number > 0 and < 10')
  else:
    try:
      raise RuntimeError
    except RuntimeError:
      print('10')

error_func()

#Написать функцию которая принимает на вход список, если все объекты -
#int, сортирует его. Иначе выбрасывает ValueError.
 
def my_list (*numbers):
    new_list = []
    for number in numbers:
        if type(number) == int:
            new_list.append(number)
        else:
            raise ValueError()
    sort_list = sorted(new_list)
    return sort_list
print(my_list(22, 3, 55, 6))


#Написать функцию которая принимает словарь,
# преобразует все ключи словаря к
#строкам и возвращает новый словарь.
#version1 work, but not good
 
my_dict = {1: 'one' , 2: 'two'}
def f_dict(x):
    new_dict = {}
    for item in x:
        key = str(item)
        value = x.get(item)
        new_dict.update({key: value})
    return new_dict
    print ('Создали новый словарь: ', new_dict)
print(f_dict(my_dict))

#Написать функцию которая принимает
#список чисел и возвращает их произведение.
 
def multy(*nums):
    i = 1
    for x in nums:
        i *= x
        print(i)
    return i
multy(2, 3, 5, 1, 6)
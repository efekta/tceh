# Создать лист из 6 любых чисел. Отсортировать его по возрастанию
# l = [26, 49, 6, 1, 10, 100]
# l.sort()
# print(l)

# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
# d = {
#     5 : '5',
#     12 : 'string',
#     1 : '100',
#     0 : '2',
#     124 : '30'
# }
# for key, value in d.items():
#     print(key, value)
# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
# t = (1.5, 6.5, 1.2, 15.9, 99.1, 874.4, 4.6, 8.89, 1090.67, 55.0)
# print(min(t))
# print(max(t))

# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'
first_list = ['Earth', 'Russia', 'Moscow']
new_list = str(first_list[0]) + ' -> ' + str(first_list[1] + ' -> ' + str(first_list[2]) + ' -> ')
print(new_list)


# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
s = '/bin:/usr/bin:/usr/local/bin'
print(s.split(':'))



# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
a = 1
b = 100
for i in range(a, b+1):
    if i % 7 == 0:
        print('число {} делимо на 7!'.format(i))
    else:
        print('число {} не делимо на 7'.format(i))

# Создать матрицу любых чисел 3 на 4,
# сначала вывести все строки, потом все столбцы
matrix = [
    [11, 22, 33],
    [55, 66, 77],
    [88, 99, 100],
    [111, 999, 555]
]
a = []
b = []
c = []

for i in matrix:
    print(row)
for col in matrix:
    a.append(col[0])
    b.append(col[1])
    c.append(col[2])
print(a)
print(b)
print(c)

# or
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print('Выводим строки\n')
for col in range(len(matrix)):
    print('\n')
    for string in range(len(matrix[col])):
        print(matrix[col][string], end=' ')

print('Выводим колонки\n')
for string in range(len(matrix[col])):
    print('\n')
    for col in range(len(matrix)):
        print(matrix[col][string], end=' ')

# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
l = [True, 'some text', None, 177, 1.5, [1,2,3,]]
for i in l:
    print('объект: ' + str(i) + ' - > имеет индекс: ' + str(l.index(i)))
# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
l = [555, 'to-delete', False, None, 'to-delete', 'some text', 'to-delete', {1:'1'}]
for item in l:
    if item == 'to-delete':
        l.remove(item)
print(l)
# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
# a = 10
# while a != 0:
#     a -= 1
#     print(a)

for i in range(10, 0, -1): # от 10 до 1 с шагом -1, т.е. с 1 - ого до последнего элемента
    print(i)
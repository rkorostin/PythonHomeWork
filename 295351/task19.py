# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

k = randint(2, 7)
print(f'k = {k}') # k = 4

#Список множителей -> [5, 0, 8, 10, 9]
factors = [randint(0, 10) for i in range(k + 1)]
while factors[0] == 0:
    factors[0] = randint(1, 10)

#Список из элементов '*x^' и '*x' -> ['*x^', '*x^', '*x^', '*x']
variables = ['*x^'] * (k - 1) + ['*x']

#Список из степеней k -> [4, 3, 2]
degrees = [i for i in range(k, 1, -1)]

#Список polynomial. Помещаю в него агрегируемые элементы из списков factors, variables и degrees
#Если при агрегации элементов из трех списков элемент отсутсвтует, то заменяю его '' (fillvalue='')
#Если элемент из списка factors равен 0, то агрегируемый элемент в список polynomial не кладу
# -> [[5, '*x^', 4], [8, '*x^', 2], [10, '*x', ''], [9, '', '']]
polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(factors, variables, degrees, fillvalue='') if a != 0]

#Добавляю ' + ' -> [[5, '*x^', 4, ' + '], [8, '*x^', 2, ' + '], [10, '*x', '', ' + '], [9, '', '', ' + ']]
for i in polynomial:
    i.append(' + ')

#Переделываю список polynomial в единую последовательность
# [5, '*x^', 4, ' + ', 8, '*x^', 2, ' + ', 10, '*x', '', ' + ', 9, '', '', ' + ']
polynomial = list(itertools.chain(*polynomial))

#Заменяю последний элемент ' = 0'
# [5, '*x^', 4, ' + ', 8, '*x^', 2, ' + ', 10, '*x', '', ' + ', 9, '', '', ' = 0']
polynomial[-1] = ' = 0'

#Меняю тип всех элементов списка polynomial на str, если встречается 1*x, то заменяю его на х
polynomial = ("".join(map(str, polynomial)).replace('1*x', 'x'))
print(polynomial)

with open('file.txt', 'w') as data:
    data.write(f'k = {k}\n')
    data.write(polynomial)
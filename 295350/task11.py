"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lst)
#
# lst2 = lst[1::2]
#
# sum_elements = 0
# for i in range(0, len(lst2)):
#     sum_elements += lst2[i]
#
# print(sum_elements)

from random import randint
lst = [randint(0,20) for i in range(randint(5,10))]
print((lst))
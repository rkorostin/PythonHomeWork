"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

import random

num = int(input("Введите кол-во элементов в списке: "))

lst = []
for i in range(num):
    el = round(random.uniform(-num, num + 1), 2)
    lst.append(el)
lst.append(random.randint(-num, num + 1))
print(lst)

lst2 = []
for i in range(0, len(lst)):
    if isinstance(lst[i], float):  # Исключаем все integer
        fractional_part = abs(round((lst[i] - int(lst[i])), 2))  # Берем модуль всех float элементов
        lst2.append(fractional_part)
lst2 = sorted(lst2)  # Сортируем список, чтобы потом от максимального вычесть минимальный

for i in range(0, len(lst2)):
    difference = round((lst2[-1] - lst2[0]),2)  # Список отсортирован по убыванию
    #т.е. максимальный элемент находится справа, а минимальный - слева.
print(difference)

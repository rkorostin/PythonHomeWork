"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
import random

num = int(input("Введите кол-во элементов в списке: "))

lst = []
for i in range(num):
    lst.append(random.randrange(-num, num + 1))
print(lst)

lst2 = []
lst_mid = int((len(lst) + 1) / 2)  # Определение длины второго списка

for i in range(0, lst_mid):
    lst2.append(lst[i] * lst[-i - 1])

print(lst2)

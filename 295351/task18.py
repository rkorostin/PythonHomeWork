# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


origin_list = [randint(0,9) for i in range(20)]
print(origin_list)

non_repeating_list = [i for i in set(origin_list)]
print(non_repeating_list)
"""
Реализуйте алгоритм перемешивания списка.
"""
original_list = list(range(10))

print("Оригинальный список: ")
print(original_list)

import random
def AlgorithmMixList(first_list):
    # Создаем копию оригинального списка
    second_list = first_list[:]
    for i in range(len(second_list)):
        # Генерируем случайный индекс
        index_random = random.randint(0, len(second_list) - 1)
        # Перемешиваем элементы списка
        temp = second_list[i]
        second_list[i] = second_list[index_random]
        second_list[index_random] = temp
    return second_list

mixed_list = AlgorithmMixList(original_list)

print("Перемешанный список по методу AlgorithmMixList : ")
print(mixed_list)

####################### Через shuffle #######################

copy_list = original_list[:]
random.shuffle(copy_list)

print("Перемешанный список по методу shuffle: ")
print(copy_list)
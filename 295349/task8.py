"""
Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
Пример:
Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
Сумма 9.06
"""
# Для простоты не делаю проверку на вводимый тип данных (что не строка).
# Не делаю проверку на отрицательное число.
# Считаем, что вводят целое положительное число

num = int(input("Введите число:"))

i = 1
array = []
while i <= num:
    subsequence = (1 + 1 / i) ** i
    subsequence = float('{:.2f}'.format(subsequence))
    # print(subsequence)
    # array = [subsequence for i in range(num)]
    array.append(subsequence)
    i += 1
print(array)

dictionary = {}

for i in range(num):
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)

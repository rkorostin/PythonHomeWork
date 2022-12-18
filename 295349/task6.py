"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
"""

num = input("Введите число:")  # Получаем данные типа string

# if '-' in num:
#     num = num.replace('-', '')  # На случай, если ввели отрицательное число

for symbol in ['-', '.']:
    if symbol in num:
        num = num.replace(symbol, "")

num_revers = num[::-1]  # Переворачиваем наоборот введённое значение

num = int(num_revers)  # Преобразуем в integer
sumNumbers = 0
while num > 0:  # Для подсчета суммы цифр в заданном числе берем операции деления и взятия остатка
    sumNumbers += num % 10
    num //= 10

print(sumNumbers)

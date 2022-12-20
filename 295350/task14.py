"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

num = int(input("Введите число: "))

lst = []

if num == 0:
    lst.append('0')
else:
    while num != 0:
        lst.append(str(num % 2))
        num //= 2

lst2 = lst[::-1]

print(" ".join(lst2))


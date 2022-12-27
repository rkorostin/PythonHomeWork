# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))

result = []
factor = 2
while 4 <= n:
    if n % factor == 0:
        result.append(factor)
        n //= factor
    else:
        factor += 1
if n > 1:
    result.append(n)

print(result)
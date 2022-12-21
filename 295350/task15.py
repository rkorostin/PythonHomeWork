"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
f(n)=f(n-2) + f(n-1) - для положительных

f(n)=f(n+2) - f(n+1) - для отрицательных

k:   -9  -8  -7  -6  -5  -4  -3  -2  -1  0  1  2  3  4  5  6  7   8   9
fib: 34 -21  13  -8   5  -3   2  -1   1  0  1  1  2  3  5  8  13  21  34

"""

k = int(input('Введите число: '))

lst_fib = []

if k == 0:
    lst_fib = [0]

# Для положительных
a = 1
b = 1
for i in range(k):
    lst_fib.append(a) # Первым действие вставляем значение "а" в список, а затем выщитываем новое значение "а"
    temp = a  # храним значение "a" во временной переменной
    a = b  # значение "a" уже в списке, поэтому приравниваем новое значение, равное "b"
    b = temp + a  # следующее значение равно сумме прошлого и текущего значения "a"

#Для отрицательных
a = 0
b = 1
for i in range(k):
    lst_fib.insert(0, a) # Каждый раз вставляем значение "a" на позицию с индексом 0
    temp = a
    a = b
    b = temp - a

print(lst_fib)

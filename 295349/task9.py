"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
"""
import random


# with open('file.txt', 'w') as data:
#     data.write('2\n')
#     data.write('4\n')
#     data.write('6')

# Функция, которая создаёт file.txt и отправляет в него рандомные числа
def post_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(-number, number + 1)}\n")


# Все данные в file.txt - это данные типа string.
# Считываем данные из file.txt, преобразуем их в integer и создаём из них список (lst_indexs)
def get_file():
    with open('file.txt', 'r') as data:
        lst_indexs = list(int(i) for i in data.readlines())
    return lst_indexs


num = int(input("Введите число N: "))
given_list = [i for i in range(-num, num + 1)]  # Создаём список от -N до N

post_file(num)  # Создаём file.txt. В нём будет {num} строк. В каждой строке рандомное число в диапазоне от -N до N
lst_index = get_file()  # Список чисел из file.txt

multiplication = 1  # Произведение по умолчанию равно 1

# Умножение элементов заданного списка, которые находятся на позициях(file.txt)
for i in range(len(lst_index)):
    multiplication *= given_list[lst_index[i]]

# Вывод в терминал для читабельности и понимания того, что происходит
print(f"Заданный список от -N до N: {given_list}")

with open('file.txt', 'r') as data:
    print(f"Данные из file.txt: \n{data.read()}")

print(f"Произведение элементов из списка, которые находятся на позициях(file.txt) = {multiplication}")
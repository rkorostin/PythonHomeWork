""" 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:

- 6 -> да
- 7 -> да
- 1 -> нет  """

print('Проверка дня недели на выходной. Проверка через число. Например, 1 - понедельник, 2 - вторник и т.д.')

def InputNumbers(inputTextFromUser):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputTextFromUser}"))
            is_OK = True
        except ValueError:
            print("Ошибка. Требуется ввод целого числа")
    return number

def CheckNumber(num):
    if 6 <= num <= 7:
        print(f'{num} -> Да')
    elif 0 < num < 6:
        print(f'{num} -> Нет')
    else:
        print(f'{num} -> число вне пределов 7 дней')

CheckNumber(InputNumbers("\nВведите число: "))
"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон
возможных координат точек в этой четверти (x и y)
"""

print('Поиск диапазон координат по заданной четветри на плоскости')

def DefinePlane(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{inputText}'))
            is_OK = True
            if number < 1 or number > 4:
                is_OK = False
                print("Всего четыре плоскости. Укажите номер от 1 до 4 ")
        except ValueError:
            print("Ошибка. Требуется ввод целого числа")
    return number

def CheckCoordinate(numberPlane):
    coordinate = 'X>0, Y<0'
    if numberPlane==1:
        coordinate = 'X>0, Y>0'
    elif numberPlane==2:
        coordinate = 'X<0, Y>0'
    elif numberPlane==3:
        coordinate = 'X<0, Y<0'
    print(f'Координаты для {numberPlane}-й плоскости -> {coordinate}')


CheckCoordinate(DefinePlane('Введите номер четверти (от 1 до 4):'))
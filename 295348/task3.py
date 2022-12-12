"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

"""

print('Поиск четверти плоскости или оси по заданным координатам')

# def inputNumbersFromUser(x):
#     list = []
#     listXYZ = ["X", "Y"]
#     for i in range(x):
#         list.append(input(f'Введите значение {listXYZ[i]}: '))
#     return list

def InputСoordinateFromUser(x):
    list = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f'Введите {i+1}-ю координату: '))
                list[i] = number
                is_OK = True
                if list[i] == 0:
                    is_OK = False
                    print("Координата соответствует одной из оси. Введите другую координату, неравную 0 ")
            except ValueError:
                print("Ошибка. Требуется ввод целого числа")
    return list

def CheckPlane(xy):
    plane = 4
    if xy[0] > 0 and xy[1] > 0:
        plane = 1
    elif xy[0] < 0 and xy[1] > 0:
        plane = 2
    elif xy[0] < 0 and xy[1] < 0:
        plane = 3
    print(f"Точка находится в {plane} четверти плоскости")

CheckPlane(InputСoordinateFromUser(2))
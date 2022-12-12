"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

def InputCoordinate(x):
    list = []
    listXY = ["A", "B"]
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите {i+1}-ю координату для точки {listXY[i]}: "))
                list.append(number)
                is_OK = True
            except ValueError:
                print("Ошибка! Вводить надо целые числа")
    return list

def Distance(a, b):
    result = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return str(result)

print("Координаты точки А")
pointA = InputCoordinate(2)
print("Координаты точки В")
pointB = InputCoordinate(2)

print(f'Длина отрезка: {Distance(pointA,pointB)[:4]}')


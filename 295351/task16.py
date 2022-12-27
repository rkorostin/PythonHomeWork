# Вычислить число pi c заданной точностью d
# Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d <= 10^(-10)


# Вывод pi через math
import math
from math import pi

print(pi)

# Формула Бэйли — Боруэйна — Плаффа

degree = 100
my_pi = sum(1/16**n*(4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6)) for n in range(degree))

print(my_pi)
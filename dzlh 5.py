#1 Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. Вычисления оформить в виде процедуры.
import math
def minimal_angle(x1, x2, y1, y2, z1, z2):
    angle_x = math.atan2(x2, x1)
    angle_y = math.atan2(y2, y1)
    angle_z = math.atan2(z2, z1)
    min_angle = min(angle_x, angle_y, angle_z)
    if min_angle == angle_x:
        return "X", (x1, x2)
    elif min_angle == angle_y:
        return "Y", (y1, y2)
    else:
        return "Z", (z1, z2)
x1, x2 = map(float, input("Введите координаты точки X (x1 x2): ").split())
y1, y2 = map(float, input("Введите координаты точки Y (y1 y2): ").split())
z1, z2 = map(float, input("Введите координаты точки Z (z1 z2): ").split())
result = minimal_angle(x1, x2, y1, y2, z1, z2)
print(f"Точка с минимальным углом: {result[0]} с координатами {result[1]}")


#2 Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.
n = int(input('Введите значение:'))
k = 0
for i in range(1, n + 1):
    binary = bin(i)[2:]
    if binary == binary[::-1]:
        j = i
        k += 1
        print(F'(Ваш по счету полиндром:{k}, Соотвествующее ему знание:{j}')
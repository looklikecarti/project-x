#ДЗ
#1 Вычислить и вывести на экран длину окружности и площадь круга одного и того же заданного радиуса R, который необходимо ввести с клавиатуры в сантиметрах. Результаты должны округляться до сотых.
import math
p = math.pi
const = 2
radius = int(input('Введите радиус:'))
large = const * p * radius
square = p * radius ** 2
print('Длина окружности:', round(large, 2), 'Площадь окружности:', round(square, 2))


#2 Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. Выведите значения переменных на экран до и после замены.
x = str(input('Введите значение x:'))
y = str(input('Введите значение y:'))
intvertX = x.replace(x, y)
intvertY = y.replace(y, x)
print('Начальные значения:', x, y)
print('Новые значения:', intvertX, intvertY)


#3 Вычислить и вывести на экран период колебания маятника длиной L с точностью до сотых. Для рассчетов использовать формулу T = 2π√(L/g), где g – ускорение свободного падения (9.81 м/c2). Значение длины маятника в метрах необходимо ввести с клавиатуры.
import math
g = 9.81
p = math.pi
L = int(input('Введите длину маятника (метры):'))
T = 2 * p * math.sqrt(L / g)
print('Период колебания маятника', round(T, 2))


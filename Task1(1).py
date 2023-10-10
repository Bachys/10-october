"""
Задание 1
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
■ Проверка на равенство радиусов двух окружностей
(операция = =);
■ Сравнения длин двух окружностей (операции >, <,
<=,>=);
■ Пропорциональное изменение размеров окружности,
путем изменения ее радиуса (операции + - += -=).
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circleLen(self):
        return self.radius * math.pi * 2

    def __str__(self):
        return "Радиус окружности {}, длинна окружности {}".format(self.radius, self.circleLen())

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.circleLen() > other.circleLen()

    def __lt__(self, other):
        return self.circleLen() < other.circleLen()

    def __ge__(self, other):
        return self.circleLen() <= other.circleLen()

    def __le__(self, other):
        return self.circleLen() >= other.circleLen()

    def __add__(self, other):
        return self.radius + other

    def __iadd__(self, other):
        self.radius  += other
        return self

    def __isub__(self, other):
        self.radius  -= other
        return self


c1 = Circle(5)
c2 = Circle(6)
print(c1)
print(c2)

# Проверка на равенство окружностей
if c1 == c2:
    print('Радиусы равны')
else:
    print('Радиусы не равны')

# Сравнение длинн окружностей
print(c1 > c2)  # Магический метод больше __gt__
print(c1 < c2)  # Магический метод меньше __lt__
print(c1 <= c2)  # Магический метод меньше либо равно __ge__
print(c1 >= c2)  # Магический метод больше либо равно __le__

# Пропорциональные изменения размеров окружностей
print(c1 + 2)

c1 += 5
print(c1)
c1 -= 2
print(c1)

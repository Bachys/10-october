"""
Задание 2
Создайте класс Complex (комплексное число). Более
подробно ознакомиться с комплексными числами можно
по ссылке.
Создайте перегруженные операторы для реализации
арифметических операций для по работе с комплексными
числами (операции +, -, *, /).
"""


class Complex:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+ {self.b}i"

    def __add__(self, other):
        return f"{self.a + other.a}+ {self.b + other.b}i"

c1 = Complex(1, 2)
c2 = Complex(2 , 1)
print(c1)
print(c2)
print(c1 + c2)
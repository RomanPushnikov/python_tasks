# '5. Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.'

x = int(input('Катет X = '))
y = int(input('Катет Y = '))

print('Гипотенуза =', (((x ** 2) + (y ** 2)) ** (1 / 2)))
print('Площадь =', (x * y) / 2)

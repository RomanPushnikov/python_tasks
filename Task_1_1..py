# "1. Даны 2 действительных числа a и b. Получить их + - и *"

a = int(input('Введите число: '))
b = int(input('Введите второе число: '))
act = input('Введите + или - или *: ')

if act == '+':
    print('Сумма =', a + b)
else:
    if act == '-':
        print('Разность =', a - b)
    else:
        if act == '*':
            print('Произведение =', a * b)
        else:
            print("Error.")

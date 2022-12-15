""" Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль."""


def function_inter():
    while True:
        try:
            x = float(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def div_2(a1, a2):
    try:
        res = a1 / a2
    except ZeroDivisionError:
        print("Error!")
    else:
        return res


print('Введите первое число  : ')
namber_1 = function_inter()
print('Введите второе число  : ')
namber_2 = function_inter()
print(f'Результат деления {namber_1} на {namber_2} равен : '
      f'{div_2(namber_1, namber_2)}')

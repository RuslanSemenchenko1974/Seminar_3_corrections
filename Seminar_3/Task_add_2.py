"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""


def function():
    while True:
        try:
            x = int(input("Введите количество элемнтов массива : "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def function_2():
    while True:
        try:
            x = float(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


qty = function()
my_list = list()
for i in range(qty):
    print(f'Введите {i + 1} элемент : ')
    i_namber = function_2()
    my_list.append(i_namber)
print(my_list)
for i in range(len(my_list) // 2):
    print(f'{my_list[i]} * {my_list[len(my_list) - 1 - i]} = '
          f'{my_list[i] * my_list[len(my_list) - 1 - i]}')

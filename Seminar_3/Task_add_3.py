"""Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов."""


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
max_el, min_el = my_list[0] - int(my_list[0]), my_list[0] - int(my_list[0])

for i in range(len(my_list)):
    if my_list[i] - int(my_list[i]) > max_el:
        max_el = my_list[i] - int(my_list[i])
    if my_list[i] - int(my_list[i]) < min_el:
        min_el = my_list[i] - int(my_list[i])
print(f'Разница между максимальным и минимальным значением дробной части '
      f'элементов : {max_el} - {min_el} = {max_el - min_el}')

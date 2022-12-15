"""Задайте список из нескольких чисел. Напишите программу, которая найдёт
сумму элементов списка, стоящих на нечётной позиции."""


def function():
    while True:
        try:
            x = int(input("Введите количество элемнтов массива :"))
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
our_sum = 0
i = 0
while i < len(my_list):
    our_sum += my_list[i]
    i += 2
print(f"Сумма элементов стоящих на нечётной позиции : {our_sum}")

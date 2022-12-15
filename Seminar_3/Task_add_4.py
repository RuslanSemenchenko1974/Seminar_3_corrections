"""Напишите программу, которая будет преобразовывать десятичное число в
двоичное."""


def function():
    while True:
        try:
            x = int(input("Введите число : "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


us_namber = function()
binary_number = []
while us_namber > 1:
    temp = us_namber % 2
    binary_number.append(temp)
    us_namber = us_namber // 2
    if us_namber == 1:
        binary_number.append(1)
binary_number.reverse()
print(binary_number)

"""Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""

def function():
    while True:
        try:
            x = int(input("Введите число : "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_1(n):
    if n == 1:
        return 1
    if n == 2:
        return -1
    else:
        return -fibonacci_1(n - 1) + fibonacci_1(n - 2)

us_namber = -abs(function())
us_namber_up = abs(us_namber)
while us_namber <= us_namber_up:
    if us_namber < 0:
        print(f'{us_namber} : {fibonacci_1(abs(us_namber))}')
    else:
        print(f'{us_namber} : {fibonacci(us_namber)}')
    us_namber += 1

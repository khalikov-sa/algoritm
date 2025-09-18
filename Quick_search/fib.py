def fibonacci(n):
    """Вычисление n-го числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(input("Введите номер числа Фибоначчи: "))))


"""
Стек для n = 5:
fibonacci(5)
> fibonacci(4) + fibonacci(3)
> (fibonacci(3) + fibonacci(2)) + (fibonacci(2) + fibonacci(1))
> ((fibonacci(2) + fibonacci(1)) + (fibonacci(1) + fibonacci(0))) + ((fibonacci(1) + fibonacci(0)) + 1)
> (((fibonacci(1) + fibonacci(0)) + 1) + (1 + 0)) + ((1 + 0) + 1)
> (((1 + 0) + 1) + 1) + (1 + 1)
> ((1 + 1) + 1) + 2
> (2 + 1) + 2
> 3 + 2 = 5
"""
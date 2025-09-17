def factorial(n):
    ''' Вычисляет факториал числа n '''    
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        factorial_value = 1
    else:
        factorial_value = n * factorial(n - 1)
    return factorial_value

if __name__ == "__main__":
    try:
        number = int(input("Введите неотрицательное целое число: "))
        print(f"Факториал {number} равен {factorial(number)}")
    except ValueError as e:
        print(e)
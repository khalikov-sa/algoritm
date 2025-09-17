def summ(arr):
    summ = arr[0]
    for i in arr[1:]:
        summ += i
    return summ


if __name__ == "__main__":
    try:
        arr = list(map(int, input("Введите числа через пробел: ").split()))
        if not arr:
            raise ValueError("Список не должен быть пустым")
        print(f"Сумма чисел: {summ(arr)}")
    except ValueError as e:
        print(e)
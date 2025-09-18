from random import randint

def search_max(arr):
    """Поиск максимального элемента в массиве с помощью рекурсии."""
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = search_max(arr[:mid])
    right_max = search_max(arr[mid:])
    return left_max if left_max > right_max else right_max


if __name__ == "__main__":
    array_size = int(input("Введите размер массива: "))
    array = [randint(0, 100) for _ in range(array_size)]
    print("Массив:", array)
    print("Максимальное значение в массиве:", search_max(array))

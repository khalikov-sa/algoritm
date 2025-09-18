from random import randint

def quick_sort(arr):
    """Быстрая сортировка массива."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    arr = [randint(0, 100) for _ in range(10)]
    print("Неотсортированный массив:", arr)
    sorted_arr = quick_sort(arr)
    print("Отсортированный массив:", sorted_arr)
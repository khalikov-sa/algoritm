from random import randint
import timeit
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def time_sort():
    """Измерение времени выполнения сортировок."""
    sizes = [10, 50, 100, 200, 500, 1000]
    merge_times = []
    bubble_times = []
    repeat = [x for x in reversed(sizes)]
    for i, size in enumerate(sizes):
        arr_1 = add_arr(size, size * 10)
        arr_2 = arr_1.copy()

        merge_sort_times = timeit.timeit(
            lambda: merge_sort(arr_1), number=repeat[i]
        )
        merge_times.append(merge_sort_times / repeat[i] * 1000)

        bubble_sort_times = timeit.timeit(
            lambda: bubble_sort(arr_2), number=repeat[i]
        )
        bubble_times.append(
            bubble_sort_times / repeat[i] * 1000
        )
    return sizes, merge_times, bubble_times

def add_arr(len_arr, max_arr):
    """Генерация массива случайных чисел."""
    arr = []
    for i in range (len_arr):
        arr.append(randint(1, max_arr))
    return arr

def plot_times(sizes, merge_times, bubble_times):
    """Построение графика времени выполнения."""
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, merge_times, "o-", label="Сортировка слиянием")
    plt.plot(sizes, bubble_times, "o-", label="Сортировка пузырьком")
    plt.xlabel("Размер списка")
    plt.ylabel("Время выполнения (мс)")
    plt.title("Сравнение времени сортировки")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sort_comparison.png")  # Сохраняем график в файл
    plt.show()


if __name__ == "__main__":
    len_arr = 100
    max_arr = 1000
    arr = add_arr(len_arr, max_arr)
    print(f"Исходный массив: {arr}")
    print(f"Массив после сортировки слиянием: {merge_sort(arr.copy())}")
    print(f"Массив после сортировки пузырьком: {bubble_sort(arr.copy())}")
    sizes, merge_times, bubble_times = time_sort()
    plot_times(sizes, merge_times, bubble_times)
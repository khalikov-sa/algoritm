from random import randint
import timeit
import matplotlib.pyplot as plt


def quick_sort(arr):
    """Быстрая сортировка."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
       
def insertion_sort(arr):
    """Сортировка вставками."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def time_sort():
    """Измерение времени выполнения сортировок."""
    sizes = [10, 100, 500, 1000, 5000, 10000]
    quick_times = []
    insertion_times = []
    repeat = [x for x in reversed(sizes)]
    for i, size in enumerate(sizes):
        arr_1 = add_arr(size, size * 10)
        arr_2 = arr_1.copy()

        quick_sort_times = timeit.timeit(
            lambda: quick_sort(arr_1), number=repeat[i]
        )
        quick_times.append(quick_sort_times / repeat[i] * 1000)

        insertion_sort_times = timeit.timeit(
            lambda: insertion_sort(arr_2), number=repeat[i]
        )
        insertion_times.append(
            insertion_sort_times / repeat[i] * 1000
        )
    return sizes, quick_times, insertion_times

def add_arr(len_arr, max_arr):
    """Генерация массива случайных чисел."""
    arr = []
    for i in range (len_arr):
        arr.append(randint(1, max_arr))
    return arr

def plot_times(sizes, quick_times, insertion_times):
    """Построение графика времени выполнения."""
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, quick_times, "o-", label="Быстрая сортировка")
    plt.plot(sizes, insertion_times, "o-", label="Сортировка вставками")
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
    print(f"Массив после быстрой сортировки: {quick_sort(arr.copy())}")
    print(f"Массив после сортировки вставками: {insertion_sort(arr.copy())}")
    sizes, quick_times, insertion_times = time_sort()
    plot_times(sizes, quick_times, insertion_times)
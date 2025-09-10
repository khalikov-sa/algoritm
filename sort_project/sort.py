from random import randint
import timeit
import matplotlib.pyplot as plt


# Массив из случайных чисел.
def add_arr(len_arr, max_arr):
    arr = []
    for i in range (len_arr):
        arr.append(randint(1, max_arr))
    return arr

# Сортировка пузырьком.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Сортировка вставками.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Замер времени выполнения
def time_sort():
    sizes = [100, 200, 300, 400, 500]
    bubble_times = []
    insertion_times = []
    repeat = [x for x in reversed(sizes)]
    for i, size in enumerate(sizes):
        arr_1 = add_arr(size, size * 10)
        arr_2 = arr_1.copy()

        bubble_sort_times = timeit.timeit(
            lambda: bubble_sort(arr_1), number=repeat[i]
        )
        bubble_times.append(bubble_sort_times / repeat[i] * 1000)

        insertion_sort_times = timeit.timeit(
            lambda: insertion_sort(arr_2), number=repeat[i]
        )
        insertion_times.append(
            insertion_sort_times / repeat[i] * 1000
        )
    return sizes, bubble_times, insertion_times


# График в линейном масштабе
def plot_times(sizes, bubble_times, insertion_times):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, bubble_times, "o-", label="Пузырьковая сортировка")
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
    print(f"Массив после пузырьковой сортировки: {bubble_sort(arr.copy())}")
    print(f"Массив после сортировки вставками: {insertion_sort(arr.copy())}")
    sizes, bubble_times, insertion_times = time_sort()
    plot_times(sizes, bubble_times, insertion_times)
import matplotlib.pyplot as plt
import timeit
from random import randint


# Бинарный поиск
def binary_search(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Линейный поиск
def linear_search(arr, num):
    for i, x in enumerate(arr):
        if x == num:
            return i
    return -1


# Генерация отсортированного массива
def sorted_arr(len_arr, max_arr):
    arr = sorted([randint(1, max_arr) for _ in range(len_arr)])
    return arr


# Замер времени выполнения
def time_search():
    sizes = [100, 1000, 10000, 100000]
    binary_times = []
    linear_times = []
    repeat = [x for x in reversed(sizes)]
    for i, size in enumerate(sizes):
        arr = sorted(randint(1, size * 10) for _ in range(size))
        num = arr[randint(0, size - 1)]  # Случайный элемент из массива

        binary_search_times = timeit.timeit(
            lambda: binary_search(arr, num), number=repeat[i]
        )
        binary_times.append(binary_search_times / repeat[i] * 1000)

        linear_search_times = timeit.timeit(
            lambda: linear_search(arr, num), number=repeat[i]
        )
        linear_times.append(
            linear_search_times / repeat[i] * 1000
        )
    return sizes, binary_times, linear_times


# График в линейном масштабе
def plot_times(sizes, binary_times, linear_times):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, binary_times, "o-", label="Бинарный поиск")
    plt.plot(sizes, linear_times, "o-", label="Линейный поиск")
    plt.xlabel("Размер списка")
    plt.ylabel("Время выполнения (мс)")
    plt.title("Сравнение времени поиска")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("search_comparison.png")  # Сохраняем график в файл
    plt.show()


if __name__ == "__main__":
    n = 100
    m = 100
    arr = sorted_arr(n, m)
    print(arr)
    num = int(input("Введите искомое число: "))
    print("Индекс искомого числа: ", binary_search(arr, num))
    print(
        "Время выполнения бинарного поиска 10^5: ",
        timeit.timeit(lambda: binary_search(arr, num), number=100000),
    )
    print(
        "Время выполнения линейного поиска 10^5: ",
        timeit.timeit(lambda: linear_search(arr, num), number=100000),
    )
    plot_times(*time_search())

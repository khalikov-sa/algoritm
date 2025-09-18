from random import randint

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, right, target)
        else:
            return binary_search(arr, left, mid - 1, target)
    return -1


if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    arr = [randint(1, 100) for _ in range(n)]
    arr.sort()
    target = int(input("Введите искомое число: "))
    print(arr)
    print(binary_search(arr, 0, len(arr) - 1, target))


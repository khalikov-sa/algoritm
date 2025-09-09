# Бинарный поиск
def bynary_search(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            left = mid +1
        else:
            right mid -1
    return -1

# Сортированный список
def sorted_arr(len_arr, max_arr):
    arr = []
    for i in range (len_arr):
        arr.append(randint(1, max_arr))
    arr.sort()
    return arr
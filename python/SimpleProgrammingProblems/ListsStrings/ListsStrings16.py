import random
from python.SimpleProgrammingProblems.ListsStrings.ListsStrings11 import sorted_merge


def selection_sort(items):
    length = len(items)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if items[j] < items[min_index]:
                min_index = j
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    length = len(items)
    for i in range(1, length):
        for j in range(0, i):
            if items[i] < items[j]:
                temp = items[i]
                for k in range(i - 1, j - 1, -1):
                    items[k + 1] = items[k]
                items[j] = temp
                break


def stooge_sort(items, start=0, end=-1):
    if items[end] < items[start]:
        items[end], items[start] = items[start], items[end]
    length = (end - start) % len(items) + 1
    if length >= 3:
        t = length // 3
        stooge_sort(items, start, end - t)
        stooge_sort(items, start + t, end)
        stooge_sort(items, start, end - t)


def partition(items, left, right, pivot_index):
    pivot_value = items[pivot_index]
    items[pivot_index], items[right] = items[right], items[pivot_index]
    store_index = left
    for i in range(left, right):
        if items[i] <= pivot_value:
            items[i], items[store_index] = items[store_index], items[i]
            store_index += 1
    items[store_index], items[right] = items[right], items[store_index]
    return store_index


def quick_sort_recursion(items, left, right):
    if left < right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(items, left, right, pivot_index)
        quick_sort_recursion(items, left, pivot_index - 1)
        quick_sort_recursion(items, pivot_index + 1, right)


def quick_sort(items):
    quick_sort_recursion(items, 0, len(items) - 1)


def merge_sort(items):
    length = len(items)
    if length <= 1:
        return
    middle = length // 2
    left = items[:middle:]
    right = items[middle::]
    merge_sort(left)
    merge_sort(right)
    list_merge = sorted_merge(left, right)
    for i in range(length):
        items[i] = list_merge[i]

if __name__ == "__main__":
    array = [random.randint(1, 100) for i in range(10)]
    print(array)

    array_copy = array.copy()
    selection_sort(array_copy)
    print(array_copy)
    print(array)

    array_copy = array.copy()
    insertion_sort(array_copy)
    print(array_copy)
    print(array)

    array_copy = array.copy()
    stooge_sort(array_copy)
    print(array_copy)
    print(array)

    array_copy = array.copy()
    merge_sort(array_copy)
    print(array_copy)
    print(array)

    array_copy = array.copy()
    quick_sort(array_copy)
    print(array_copy)
    print(array)

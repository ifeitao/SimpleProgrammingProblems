def binary_search(items, item):
    start = 0
    length = len(items)
    end = length - 1
    while True:
        middle = (start + end) // 2
        found = items[middle]
        if item == found:
            return middle
        elif item < found:
            if middle == start:
                return ~middle
            else:
                end = middle - 1
        else:
            if middle == end:
                if end == length - 1:
                    return length
                else:
                    return ~(middle + 1)
            else:
                start = middle + 1


print(binary_search([1], 1))
print(~(binary_search([1], 0.5)))
print(binary_search([1], 1.5))

print(binary_search([1, 2], 1))
print(binary_search([1, 2], 2))
print(~(binary_search([1, 2], 0.5)))
print(~(binary_search([1, 2], 1.5)))
print(binary_search([1, 2], 2.5))

print(binary_search([1, 2, 3], 1))
print(binary_search([1, 2, 3], 2))
print(binary_search([1, 2, 3], 3))
print(~(binary_search([1, 2, 3], 0.5)))
print(~(binary_search([1, 2, 3], 1.5)))
print(~(binary_search([1, 2, 3], 2.5)))
print(binary_search([1, 2, 3], 3.5))

print(binary_search([1, 3, 5, 7, 9], 1))
print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9], 5))
print(binary_search([1, 3, 5, 7, 9], 7))
print(binary_search([1, 3, 5, 7, 9], 9))
print(~(binary_search([1, 3, 5, 7, 9], 0)))
print(~(binary_search([1, 3, 5, 7, 9], 2)))
print(~(binary_search([1, 3, 5, 7, 9], 4)))
print(~(binary_search([1, 3, 5, 7, 9], 6)))
print(~(binary_search([1, 3, 5, 7, 9], 8)))
print(binary_search([1, 3, 5, 7, 9], 10))

def fibonacci_list_recursion(n):
    if n == 1:
        items = [1]
    elif n == 2:
        items = [1, 1]
    else:
        items = fibonacci_list_recursion(n - 1)
        items.append(items[n - 3] + items[n - 2])
    return items


def fibonacci_list(n):
    if n == 1:
        items = [1]
    elif n == 2:
        items = [1, 1]
    else:
        items = [1, 1]
        for i in range(2, n):
            items.append(items[i - 2] + items[i - 1])
    return items

if __name__ == "__main__":
    print(fibonacci_list(100))
    print(fibonacci_list_recursion(100))

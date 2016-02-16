def for_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def while_sum(numbers):
    length = len(numbers)
    total = 0
    i = 0
    while i < length:
        total += numbers[i]
        i += 1
    return total


def recursion_sum(numbers):
    length = len(numbers)
    if length == 0:
        return 0
    elif length == 1:
        return numbers[0]
    else:
        return numbers[0] + recursion_sum(numbers[1::])

if __name__ == "__main__":
    my_numbers = [2, 3, 5, 7, 9]
    print(for_sum(my_numbers), while_sum(my_numbers), recursion_sum(my_numbers))

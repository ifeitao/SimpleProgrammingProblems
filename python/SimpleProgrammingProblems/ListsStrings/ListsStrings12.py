def swap_rotate(items, rotate_length):
    length = len(items)
    rotate_length %= length
    count = 0
    while True:
        swap_length = min(rotate_length, length - rotate_length)
        if swap_length == 0:
            break
        for i in range(swap_length):
            items[length - 1 - i], items[rotate_length - 1 - i] = items[rotate_length - 1 - i], items[length - 1 - i]
        count += swap_length
        if rotate_length > swap_length:
            rotate_length -= swap_length
        length -= swap_length
    return count


if __name__ == "__main__":
    for p in range(1, 20):
        for q in range(1, p + 1):
            array = list(range(1, p + 1))
            print("shift_length={0}, swap_count={1}, result={2}".format(q, swap_rotate(array, q), array))


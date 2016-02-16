def running_total(items):
    total_list = []
    total = 0
    for item in items:
        total += item
        total_list.append(total)
    return total_list

if __name__ == "__main__":
    numbers = [1, 3, 11, 5, 7, 9]
    print(running_total(numbers))

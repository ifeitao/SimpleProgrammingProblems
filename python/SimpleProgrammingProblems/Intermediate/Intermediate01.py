def compute(symbols):
    numbers = []
    number = 0
    sign = 1
    for item in symbols:
        if item == '+':
            numbers.append(number)
            number = 0
            sign = 1
        elif item == '-':
            numbers.append(number)
            number = 0
            sign = -1
        else:
            if sign == 1:
                number = number * 10 + int(item)
            else:
                number = number * 10 - int(item)
    numbers.append(number)
    return sum(numbers)


def check_all():
    for i in range(0, 3 ** 8):
        symbols = []
        j = i
        for digit in range(1, 9):
            symbols.append("%s" % digit)
            remainder = j % 3
            if remainder == 0:
                symbols.append("+")
            elif remainder == 1:
                symbols.append("-")
            j //= 3
        symbols.append("9")
        if compute(symbols) == 100:
            print("{0}=100".format("".join(symbols)))


if __name__ == "__main__":
    check_all()

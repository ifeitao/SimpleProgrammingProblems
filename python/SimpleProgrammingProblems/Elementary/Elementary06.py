import sys

while True:
    number = int(input("Please input a number:\n"))
    mode = input("Need sum or product? Please input s for sum, p for product, or e for exit:\n")
    if mode in ("sum", "s"):
        total = sum(range(1, number + 1))
        print(total)
    elif mode in ("product", "p"):
        product = 1
        for i in range(1, number + 1):
            product *= i
        print(product)
    elif mode in ("exit", "e"):
        sys.exit()

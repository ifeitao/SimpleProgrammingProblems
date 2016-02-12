number = int(input("Please input a number:\n"))
total = 0
for i in range(1, number + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

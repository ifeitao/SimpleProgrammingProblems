import random

N = int(input("The computer will produce a number between 1 and N, please input N:\n"))
print("The computer has  produced a number, please guess:\n")
number = random.randint(1, N)
total = 0
last_guess = 0
while True:
    guess = int(input())
    if last_guess != guess:
        last_guess = guess
        total += 1
    if guess < number:
        print("Too small, please guess again.")
    elif guess > number:
        print("Too big, please guess again.")
    else:
        print("After {0} guesses, you finally right".format(total))
        break

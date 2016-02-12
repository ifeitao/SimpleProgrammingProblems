primes = []
i = 2
while True:
    is_prime = True
    for j in primes:
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
        primes.append(i)
    i += 1 

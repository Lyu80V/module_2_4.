numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = [i for i in range(1, 16)]
primes = []
not_primes =[]
for number in numbers:
    if number == 1:
        continue
    is_primes = True
    for i in range(2, number):
        if number % i == 0:
            is_primes = False
            break
    if is_primes:
        primes.append(number)
    else:
        not_primes.append(number)
print('Primes:', primes)
print('Not Primes:', not_primes)
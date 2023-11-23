from math import floor, ceil, log




def generate_arithmetic_sequence(n, start, step):
    sequence = []
    for i in range(n):
        sequence.append(start + i * step)
    return sequence


def generate_geometric_sequence(n, start, factor):
    sequence = []
    for i in range(n):
        sequence.append(start * factor**i)
    return sequence


def generate_recursive_sequence(n, start1, start2, weight1, weight2):
    sequence = []
    sequence.append(start1)
    sequence.append(start2)
    for i in range(n - 2):
        sequence.append(weight1 * sequence[i] + weight2 * sequence[i + 1])
    return sequence


def generate_fibonacci_sequence(n):
    return generate_recursive_sequence(n, 1, 1, 1, 1)


def generate_primes_sequence(n):
    # find n primes using sieve of eratosthenes

    primes = []
    sieve = [True] * floor((n * log(n * log(n))) + 10)  # for n > 6

    for i in range(2, len(sieve)):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, len(sieve), i):
                sieve[j] = False
    return primes


def generate_binomial_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(i * (i - 1) / 2)
    return sequence


def generate_semiprimes_sequence(n):
    semiprimes = []

    sieve = [0] * ceil((n * log(n * log(n))))  # for n > 6

    for i in range(2, len(sieve)):
        if sieve[i] == 0:
            for j in range(i * i, len(sieve), i):
                sieve[j] += 1
        if sieve[i] == 2:
            semiprimes.append(i)
    return semiprimes

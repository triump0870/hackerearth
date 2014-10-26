def get_next_prime_factor(n, factor):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    for x in range(int(factor/6), int(math.sqrt(n)/6) + 1):
        if n % (6*x-1) == 0:
            return 6*x-1

        if n % (6*x+1) == 0:
            return 6*x+1

    return int(n)
print get_next_prime_factor()
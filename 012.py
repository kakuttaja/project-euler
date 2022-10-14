from eulerlib.prime_numbers import primes

def main() -> int:
    # The product of the amount of prime factors
    # for a number IS the total amount of factors
    _primes = primes(10000)
    lim = 500
    a = 0
    b = 1
    divs = 0
    while divs <= lim:
        # A triangle number is the sum of all natural numbers to its index
        # e.g. Tri2 = 1 + 2 = 3, Tri3 = 1 + 2 + 3 = 6
        (a, b) = (a + b, b + 1)
        n = a
        _ans = 1
        p_idx = 0
        while n > 1:
            # Don't want to go out of index..
            # Highly composite numbers favour as small prime factors as possible
            # while the count of these individual factors is also as small as possible.
            # 
            # Therefore, it's probably good to just try to calculate factors
            # using as few primes as possible, in my case 10 000 primes max.
            if p_idx >= len(_primes): break
            k = 1
            # Get the 'counts' of individual primes that are the factors of this number
            while n % (_primes[p_idx]**k) == 0:
                k += 1
            # Check if prime is a factor of this number
            # and add the count of the prime factor into answer product.
            # 
            # Remember to also divide the number by the factor**count
            # to start working on the next prime factor _primes[p_idx + 1].
            if n % _primes[p_idx] == 0:
                _ans *= k
                n = n // _primes[p_idx] ** (k - 1)
            p_idx += 1
        divs = _ans
    return a

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

from eulerlib.prime_numbers import primes

def phi(n: int, primes: list[int]) -> int:
    if n < 1: return 0
    if n == 1: return 1
    if n in primes: return n - 1
    prod = n
    for p in primes:
        if p * 2 > n:
            return prod
        if n % p:
            continue
        prod *= (1 - 1/p)
    return prod

def main() -> int:
    # Inefficient as ____
    # Probably should use a brain cell
    # and look into building some list of prime factors
    # avoiding manual phi(x) calculations for every x in existence
    ans = 0
    n = 10**6
    p = primes(n)
    ans = 0
    for i in range(2, n + 1):
        a = phi(i, p)
        ans += a
    return ans


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

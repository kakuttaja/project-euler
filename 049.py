from eulerlib import primes
import itertools as it

def get_factor(n: int, primes: list[int]) -> list[int]:
    factors = []
    idx = 0
    p = primes[idx]
    while n > 1 and p < n:
        p = primes[idx]
        t = 0
        while n % p == 0:
            n /= p
            t += 1
        if t:
            factors.append((p, t))
        idx += 1
    return set(factors)

def main() -> int:
    p = primes(150000)
    start = 646
    for i in it.count(start):
        factors = get_factor(i, p)
        cont = i + 1
        if len(factors) != 4: continue
        while True:
            if cont - i == 4:
                return i
            factors2 = get_factor(cont, p)
            new_factors = factors | factors2
            if len(factors2) != 4 or len(factors & factors2) > 0:
                break
            cont += 1
            factors = new_factors
    return

if __name__ == "__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
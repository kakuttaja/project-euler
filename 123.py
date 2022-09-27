from typing import List


def prime_gen(lim: int) -> List[int]:
    primes = [True] * lim
    res = []
    for i in range(2, lim):
        if primes[i]:
            res.append(i)
            for j in range(i*i, lim, i):
                primes[j] = False
    return res

def main() -> None:
    primes = prime_gen(1000000)
    for n in range(len(primes)):
        u = (primes[n - 1] - 1)**n + (primes[n - 1] + 1)**n
        d = primes[n - 1]**2
        r = u % d
        if r > 10**10:
            print(n, "-->", r)
            return n
    return None

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
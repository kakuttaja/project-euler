from collections import defaultdict
from itertools import count
import tqdm

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_gen(n: int) -> int:
    while True:
        n += 1
        if is_prime(n):
            yield n

def factorization(n: int, primes: list, lim: int = 4):
    if is_prime(n) or n == 1:
        return [n], primes
    p = 0
    for prime in primes:
        if n % prime == 0:
            p = prime
            break
    factors = defaultdict(lambda: 0)
    while True:
        if len(factors.keys()) > lim:
            break
        while n % p == 0:
            factors[p] += 1
            n = n // p
        if n <= 1:
            break
        if p >= primes[-1]:
            i = 0
            # oh no don't want to run out of primes 
            # and end up with an IndexError
            # -> generate more
            for prime in prime_gen(p):
                primes.append(prime)
                i += 1
                if i >= 1000:
                    break
        p = primes[primes.index(p) + 1]
    return ([k * v for k, v in factors.items()], primes)

def slower_sieve():
    # The old implementation
    # using a kinda-sieve-ish-sieve
    # with the fact that w(2n) is related to w(n).
    p = [i for i in range(15000) if is_prime(i)]
    t = 4
    flist = {}
    for i in tqdm.tqdm(range(4, 135000), ascii=True, disable=False):
        skip = False
        for k in range(i, i + t):
            if flist.get(k, t) != t:
                skip = True
                for l in range(1, 20):
                    flist[2 * l * k] = flist[k] if (k * l) % 2 == 0 else flist[k] + 1
        if skip:
            continue
        factors = flist.get(i, None)
        if factors is None:
            factors, p = factorization(i, p)
            factors = len(factors)
        flist[2 * i] = factors if i % 2 == 0 else factors + 1
        factors = [factors]
        if factors[0] == t:
            for j in count(i + 1):
                f = flist.get(j, None)
                if not f:
                    f, p = factorization(j, p)
                    f = len(f)
                flist[2 * j] = f if j % 2 == 0 else f + 1
                if f == t:
                    factors.append(f)
                    continue
                break
        if len(factors) == t:
            break
    return i

def main():
    # w(2n) = w(n) + 1 if n = 1 (mod 2)
    # w(2n) = w(n) if n = 0 (mod 2)
    # Doing a similar thing to a prime sieve
    # following the w(2n) rule to avoid
    # calculating factors for every single number.
    # 
    # ..actually why not implement this in a prime sieve?
    # Sieve goes through all numbers through their factors
    # to find numbers without any, i.e., primes.
    # 
    # Could just increment factors += 1 in every pass.
    # Runs much faster.
    t = 4
    lim = int(1e6)
    divs = [0] * lim
    for i in range(2, lim):
        if divs[i] == 0:
            for j in range(2 * i, lim, i):
                divs[j] += 1
        if all(k == t for k in divs[i : i + t]):
            return i
    return slower_sieve()

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
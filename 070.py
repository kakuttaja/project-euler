import itertools as it

def prime_gen( ):
    # An optimized Erastosthenes' sieve function
    # erat2 from https://stackoverflow.com/a/3796442
    D = {  }
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D:
                x += 2*p
            D[x] = p

def prime_list(num):
    mypgen = prime_gen()
    result = []
    while True:
        p = next(mypgen)
        if p > num:
            break
        else:
            result.append(p)
    return result

def check_digits(a, b) -> bool:
    return sorted(int(i) for i in str(a)) == sorted(int(i) for i in str(b))

def phi(p1, p2) -> int:
    # phi(n) = n * T(p|n)(1 - 1/p)
    # Therefore if n = product([p]),
    # then phi(n) = product([p - 1])
    # 
    # In other words: (p1 * p2) = n,
    # phi(n) = (p1 * p2) * (1 - 1/p1) * (1 - 1/p2)
    return (p1 * p2) * (1 - 1/p1) * (1 - 1/p2)

def main():
    # To minimize phi(n), we need to minimise len(prime_factors) and maximise sum(prime_factors)
    # phi(n) function can also be made very simple, as there is no need to search for factors,
    # because we are iterating through primes to build a number.
    # 
    # To minimise len(prime_factors), only 2 primes are used to build a number.
    # 
    # As the primes must both be close to max, we want to limit the length of
    # primes, but not too much (therefore limit + 10**5), so that they are AROUND sqrt(limit)
    ans = 0
    lowest = 99999999
    limit = 10**7
    primes = prime_list(int(limit**0.5) + 10**5)
    for i in range(len(primes) - 1):
        for j in range(i + 1, len(primes)):
            p1 = primes[i]
            p2 = primes[j]
            if p1*p2 > limit: break
            n = int(phi(p1, p2))
            if check_digits(p1*p2, n):
                if (p1*p2)/n < lowest:
                    lowest = (p1*p2)/n
                    ans = p1*p2
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"Time taken: {round(perf_counter() - start, 2)}s")

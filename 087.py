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

def main():
    # Easy to brute-force, using a set to avoid duplicates.
    ans = set()
    target = 50000000
    primes = prime_list(int(target**0.5) + 1)
    for i in range(len(primes)):
        if primes[i]**2 >= target:
            break
        for j in range(len(primes)):
            if primes[j]**3 + primes[i]**2 >= target:
                break
            for k in range(len(primes)):
                a = primes[i]**2
                b = primes[j]**3
                c = primes[k]**4
                if a+b+c >= target:
                    break
                ans.add(a+b+c)
    return len(ans)

if __name__ == '__main__':
    import time
    start = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - start, 2)}s")

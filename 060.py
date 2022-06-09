import itertools as it

def is_prime(n: int) -> bool:
    # Primality test using 6k+-1 optimization.
    # https://en.wikipedia.org/wiki/Primality_test#Python
    n = int(n)
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

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

def create_pairs(primes) -> dict[int, set[int]]:
    pairs = {p: set() for p in primes}
    for i in range(len(primes) - 1):
        p = primes[i]
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if p == p2: continue
            if p == 2 or p == 5: continue
            if is_prime(str(p) + str(p2)) and is_prime(str(p2) + str(p)):
                if p not in pairs.keys():
                    pairs[p] = set([p2])
                else:
                    pairs[p].add(p2)
    return pairs

def main2():
    # Create pairs in iterations for each
    # new pair generated from the original primes[a]
    # 
    # If a pair exists after 3 new pairs are generated for primes[a],
    # it is the number that allows for a 5-prime family all concatenating to primes.
    # 
    # Though performance doesn't differ much from main(),
    # it is still prettier and more understandable code.
    ans = [999999]
    primes = prime_list(10000)
    pairs = create_pairs(primes)
    for a in range(2, len(primes)):
        if primes[a] == 5: continue
        p1 = primes[a]
        new_pairs = set(pairs[p1]) & set(pairs[p1])
        for pair1 in new_pairs:
            new_pairs2 = set(pairs[pair1]) & set(pairs[p1])
            for pair2 in new_pairs2:
                new_pairs3 = set(pairs[pair1]) & set(pairs[p1]) & set(pairs[pair2])
                for pair3 in new_pairs3:
                    new_pairs4 = set(pairs[pair1]) & set(pairs[p1]) & set(pairs[pair2]) & set(pairs[pair3])
                    if new_pairs4:
                        print("Found:", sum([p1, pair1, pair2, pair3, min(new_pairs4)]))
                        ans.append(sum([p1, pair1, pair2, pair3, min(new_pairs4)]))
    return min(ans)

def main():
    # Create list of pairs,
    # check if each next number
    # is a pair with every other number
    primes = prime_list(10000)
    pairs = create_pairs(primes)
    ans = [999999]
    for p1 in range(len(primes) - 1):
        if primes[p1] == 2 or primes[p1] == 5: continue
        for p2 in range(p1 + 1, len(primes)):
            if not primes[p2] in pairs[primes[p1]]: continue
            for p3 in range(p2 + 1, len(primes)):
                if (primes[p3] not in pairs[primes[p2]] or 
                    primes[p3] not in pairs[primes[p1]]): continue
                for p4 in range(p3 + 1, len(primes)):
                    if (primes[p4] not in pairs[primes[p2]] or 
                        primes[p4] not in pairs[primes[p1]] or 
                        primes[p4] not in pairs[primes[p3]]): continue
                    for p5 in range(p4 + 1, len(primes)):
                        if (primes[p5] not in pairs[primes[p2]] or 
                            primes[p5] not in pairs[primes[p1]] or 
                            primes[p5] not in pairs[primes[p3]] or 
                            primes[p5] not in pairs[primes[p4]]): continue
                        print("Found:", sum([primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]]))
                        ans.append(sum([primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]]))
    return min(ans)

if __name__ == '__main__':
    import time
    start = time.time()
    print(main2())
    print(f"Time taken: {round(time.time() - start, 2)}s")

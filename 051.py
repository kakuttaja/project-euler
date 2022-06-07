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

def is_prime(n: int) -> bool:
    # Primality test using 6k+-1 optimization.
    # https://en.wikipedia.org/wiki/Primality_test#Python
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

def solver(number: list[int], indices: list[int]):
    number_copy = [int(i) for i in number]
    if indices:
        primes, smallest = 0, 0
        for i in range(10):
            if len(number) - 1 in indices and i not in [1, 3, 7, 9]: continue
            if i == 0 and 0 in indices: continue
            for j in indices:
                number_copy[j] = i
            if is_prime(int(''.join([str(i) for i in number_copy]))):
                primes += 1
                if not smallest:
                    smallest = int(''.join([str(i) for i in number_copy]))
        if primes == 8:
            return True, smallest
        if len(indices) == len(number):
            return False, 0
    if indices: 
        i = max(indices)
    else: 
        i = 0
    while i < len(number):
        if i not in indices:
            indices.append(i)
            result, num = solver(number, indices)
            if result:
                return result, num
            indices.pop()
        i += 1
    return False, 0


def main():
    for p in prime_gen():
        result, num = solver([int(i) for i in str(p)], [])
        if result:
            return num
    return None

if __name__ == '__main__':
    import time
    s = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - s, 2)}s")

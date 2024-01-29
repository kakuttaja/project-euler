from itertools import count
from collections import defaultdict

def penta(k: int) -> int:
    if k == 0:
        return 0
    return int(k * (3 * k - 1) / 2)

def main():
    # Traditional memoization approach will not work for this
    # unless you'd like to increase recursion limits to 60k+.
    # 
    # Interestingly pentagonal numbers are connected to partitions
    # p(n) = SUM{ (-1)^k-1 * p(n - gk) }
    # In which every second addition to the sum is negative,
    # and numbers are done up to gk which is the highest
    # pentagonal number that is <= n, as p(n) = 0, when n < 0.
    # 
    # In other words,
    # p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7) + ...
    # up until (n - k) < 0, at which point loop is broken.
    # NOTE: two values positive -> negative -> positive -> etc.
    # Highest penta that was used in the calculation of partitions
    # was interestingly as low as P(383) = 55 392.
    partitions = defaultdict(lambda: 1)
    pentas = [[penta(i), penta(-i)] for i in range(1, 193)]
    pentas = sum(pentas, [])
    for n in count(2):
        s = 0
        for i, p in enumerate(pentas):
            if n - p < 0:
                break
            if i % 4 < 2:
                s += partitions[n - p]
            else:
                s -= partitions[n - p]
        # Funny floating-point limited precision in modulos,
        # must convert to int beforehand..
        if s % int(1e6) == 0:
            return n
        partitions[n] = s
    return

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
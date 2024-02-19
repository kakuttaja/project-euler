from time import perf_counter
import functools
import itertools as it

def main() -> int:
    # Similarly simple memoization solution.
    @functools.cache
    def F(m, n, gray=True):
        if n < m:
            return 1
        if not gray:
            return F(m, n - 1)
        t = l = 0
        while n - (m + l) >= 0:
            t += F(m, n - (m + l), False)
            l += 1
        return t + F(m, n - 1)
    for i in it.count(1):
        if F(50, i) > (10 ** 6):
            return i

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
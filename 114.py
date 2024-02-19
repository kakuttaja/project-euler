from time import perf_counter
import functools

def main() -> int:
    # Simple memoization solution.
    @functools.cache
    def F(n, gray=True):
        if n < 3:
            return 1
        if not gray:
            return F(n - 1)
        t = l = 0
        while n - (3 + l) >= 0:
            t += F(n - (3 + l), False)
            l += 1
        return t + F(n - 1)
    return F(50)

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
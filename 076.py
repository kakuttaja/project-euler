import functools

@functools.cache
def p(n: int, k: int) -> int:
    if k == 0:
        return 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    return p(n - k, k) + p(n, k - 1)

def main():
    return p(100, 99)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
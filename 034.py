import functools

@functools.cache
def f(n: int) -> int:
    if n <= 1:
        return 1
    return f(n - 1) * n

def main():
    # As individual digits are within [0, 9]
    # their factorial sums will, at some point,
    # be significantly smaller than the
    # total integer number.
    # This happens at 7 * 9! = 2540160,
    # because 8 * 9! = 2903040 (len=7)
    # and 7 * 9! (and 8 * 9!) <<<<<<< 9999999.
    ans = 0
    for n in range(3, 7 * f(9)):
        if n == sum(map(f, [int(i) for i in str(n)])):
            ans += n
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
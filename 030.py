
def main() -> int:
    # Limit is at max 99 999,
    # because the 6-number values
    # would never be able to add up high enough.
    # E.g. 6 * (9 ** 5) = 354 294 < 10**6
    limit = 5 * (9 ** 5)
    ans = 0
    i = 1000
    for i in range(1000, limit):
        result = 0
        n = i
        while n > 0:
            result += (n % 10) ** 5
            n = n // 10
        if result == i:
            ans += i
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

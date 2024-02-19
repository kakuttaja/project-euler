from time import perf_counter

def main() -> int:
    # a and n seem to be coprime
    # and n is always an odd number
    # 
    # Even n: 2a**2 + 2 = r mod a**2
    # => 2a**2 = 0 mod a**2
    # => 2a**2 + 2 = 2 mod a**2
    # Me thinks.
    # 
    # looking even further,
    # for even numbers of a
    # n = (a - 1)
    # 
    # for odd numbers of a
    # n = floor(0.5 * a) or n = floor(1.5 * a)
    # that lead to maximized remainders.
    # 
    # Also interestingly
    # the highest remainder for each a:
    # ODD: a**2 - a
    # EVEN: a**2 - 2a
    ans = 0
    for a in range(3, 1001):
        n = a - 1
        if not n % 2:
            n = int(1.5 * a) if int(1.5 * a) % 2 else a // 2
        ans += ((a - 1) ** n + (a + 1) ** n) % (a ** 2)
    return ans
    # Old brute-force approach that also misses a=3,
    # because it is the exception with set n-range.
    for a in range(3, 1001):
        best = 0
        for n in range(3, int(1.5 * a + 1), 2):
            r = ((a - 1) ** n + (a + 1) ** n) % (a ** 2)
            if r > best:
                best = r
        ans += best
    return ans + 6

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
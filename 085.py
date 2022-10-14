

def main() -> int:
    ans = (0, 0)
    diff = 999999999
    a = 0
    m = 3
    # Arbitrary limit 3e6, as the count of
    # possible m*n rectangles gets really high
    # after high enough values
    # 
    # Can also solve by checking all n-values
    # and solving the resulting quadratic equating for m.
    # 
    # The closest-to integer value of the equation
    # m**2 + m - (8e6/(n + 1)*n) = 0
    # is the m for the solution's (m, n) pair.
    while a < int(3e6):
        for n in range(2, m):
            a = int(((m + 1) * m)/2 * ((n + 1) * n)/2)
            if -1 * (int(2e6) - a) > diff:
                # The possible combinations is getting much higher
                # than previous closest guess -> start over with m += 1
                break
            if abs(int(2e6) - a) < diff:
                # Found a new closest pair (m, n)
                diff = abs(int(2e6) - a)
                ans = (m, n)
        m += 1
    return ans[0] * ans[1]

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

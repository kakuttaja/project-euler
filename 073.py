

def binary_gcd(u, v) -> int:
    # Binary GCD algorithm
    # https://en.wikipedia.org/wiki/Binary_GCD_algorithm#Implementation
    if u == 0: return v
    if v == 0: return u
    i = (u&-u).bit_length() - 1
    u >>= i
    j = (v&-v).bit_length() - 1
    v >>= j
    k = min(i, j)
    while True:
        if u > v:
            u, v = v, u
        v -= u
        if v == 0:
            return u << k
        v >>= j

def euclidean_gcd(a, b) -> int:
    # Uses the euclidean algorithm
    # https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclidean_algorithm
    if a == 1 or b == 1: return 1
    while b > 0:
        a, b = b, a % b
    return a

def main():
    # Get highest number between 2/5 and 3/7
    # In a/b < 3/7 => 7a < 3b => 7a = 3b - 1
    # Therefore highest a = (3*b-1)/7,
    # which is the closest number to 3/7.
    #
    # As the numerator a must be an integer,
    # a % 1 == 0 must be checked.
    ans = 0
    d = 1
    lower = 1/3
    while d <= 12000:
        n = 1
        while n < d/2:
            if not euclidean_gcd(n, d) == 1:
                n += 1
                continue
            if lower < n/d:
                ans += 1
            n += 1
        d += 1
    return ans

if __name__ == '__main__':
    import time
    start = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - start, 2)}s")

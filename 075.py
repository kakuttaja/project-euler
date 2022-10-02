from eulerlib.numtheory import gcd


def euclid(m: int, n: int) -> tuple[int, int, int]:
    return sum([m**2 - n**2, 2 * m * n, m**2 + n**2])

def main() -> int:
    # The question is about Pythagorean triples
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    limit = 1500000
    triples = {}
    ans = 0
    # A limit for m is sq(limit) due to the fact m**2 is squared in the formula
    # the limit could be refined even further, but it is acceptably efficient as is.
    for m in range(2, int(limit ** 0.5) + 1):
        for n in range(1, m):
            # Triple is primitive only if m and n are coprime 
            # and only one of them is even
            if (m + n) % 2 != 1 or gcd(m, n) != 1:
                continue
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            L = a + b + c
            # Loop through other triples to get every single possible
            # pythagorean triple and check for multiple sums as well
            while L <= limit:
                if L not in triples.keys():
                    triples[L] = 1
                    ans += 1
                elif triples[L] == 1:
                    triples[L] += 1
                    ans -= 1
                # Important to note that L += L would be incorrect
                # because we want to advance with a+b+c intervals
                # ...spent way too much time debugging that.
                L += a + b + c
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")


def convert_into_frac(seq):
    # Convert a simple continued fraction sequence into a single fraction a/b
    h, k = [0, 1], [1, 0]
    _h, _k = [], []
    for i, n in enumerate(seq, 2):
        h.append(n * h[i - 1] + h[i - 2])
        k.append(n * k[i - 1] + k[i - 2])
    return (h[-1], k[-1])

def main() -> int:
    # https://en.wikipedia.org/wiki/Continued_fraction#Regular_patterns_in_continued_fractions
    # e has a very nice pattern in the simple continued fraction expansion
    # with an even number (in order) spaced apart by 2 digits every time
    # [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
    limit = 100
    fracs = [2]
    for i in range(1, limit):
        if i % 3 == 2:
            fracs.append(2 * (i + 1) // 3)
        else:
            fracs.append(1)
    ans = convert_into_frac(fracs)
    return sum([int(i) for i in str(ans[0])])

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

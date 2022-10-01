
def main() -> None:
    # https://en.wikipedia.org/wiki/Periodic_continued_fraction
    # An iterative algorithm can be used to obtain consecutive components of the continued fractions
    ans = 0
    limit = 10000
    for N in range(2, limit + 1):
        if N**0.5 % 1 == 0:
            continue
        seq = list()
        a0 = int(N**0.5)
        a = int(N**0.5)
        m = 0
        d = 1
        while True:
            if a == 2*a0:
                # Repeat occurred!
                # in [a1, a2, ..., an]
                # an = 2a1, therefore when a = 2*a0, 
                # it is the last element of the unique sequence
                # https://web.math.princeton.edu/mathlab/jr02fall/Periodicity/alexajp.pdf
                break
            m = int(d * a - m)
            d = int(N - m**2)/d
            a = int((a0 + m)/d)
            seq.append(a)
        if len(seq) % 2:
            ans += 1
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

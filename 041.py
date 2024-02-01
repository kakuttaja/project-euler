
def main():
    # https://math.stackexchange.com/a/99743
    # Congruency of pandigital numbers
    # -> divisibility of n-length numbers could be
    # determined for all n = [1, 9].
    # 
    # All n except for 4 and 7 were divisible by some
    # number shared between all same n-length integers,
    # so they definitely are not prime numbers.
    # Therefore the check can be limited to numbers
    # of lengths 4, and 7, with 7 being the priority.
    # 
    # In my case, efficient primes list up to 1e7.
    lim = int(1e7)
    p = [True] * lim
    p[0] = False
    p[1] = False
    for i in range(2, lim):
        if p[i]:
            for j in range(i * i, lim, i):
                p[j] = False
    return [i for i, b in enumerate(p) if b and all([str(i).count(str(j)) == 1 for j in range(1, len(str(i)) + 1)])][-1]


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
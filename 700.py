import itertools as it

def brute_force() -> None:
    # Brute-force the starting numbers to avoid having to calculate way too high ones
    base = 1504170715041707 * 1 % 4503599627370517
    n = 1
    sum = base
    for n in it.count(1):
        new = (1504170715041707 * n) % 4503599627370517
        if new < base:
            base = new
            sum += base
        if new <= 15806432:
            # Arbitrary break-point for optimizing time spent
            break
    return sum, base

def extended_euclidean(a, n) -> int:
    # Calculate multiplicative inverses
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Computing_multiplicative_inverses_in_modular_structures
    # 
    t = 0
    newt = 1
    r = n
    newr = a
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)
    if t < 0:
        t = t + n
    return t

def main() -> int:
    # Brute-force for starting numbers to avoid very-very-very high numbers
    # 
    # Then move on to modular multiplicative inverses
    # to solve for all resulting modulos
    ans, min = brute_force()
    a = 1504170715041707
    mod = 4503599627370517
    inverse = extended_euclidean(a, mod)
    d = {}
    s = set()
    for i in range(1, min):
        d[(inverse * i) % mod] = i
        s.add(i)
    for k in sorted(d.keys()):
        if d[k] < min:
            min = d[k]
            ans += min
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    # print(sum(NUMS) - 258162)
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
from eulerlib.numtheory import Divisors

def main():
    # Prime factor-optimized method
    # Multiply all the primes together
    # with their highest powers.

    d = Divisors()
    b = 1
    prime_factors = {}
    for i in range(2, 21):
        factors = d.prime_factors(i)
        for p, q in factors:
            if p not in prime_factors:
                prime_factors[p] = q
            elif prime_factors[p] < q:
                prime_factors[p] = q
    for p, q in prime_factors.items():
        b *= (p**q)
    return b

    # Brute-force method
    limit = 20
    a = 20
    while True:
        for i in range(limit, 0, -1):
            if not a % i == 0:
                break
        else:
            return a
        a += 20

if __name__ == '__main__':
    print(main())
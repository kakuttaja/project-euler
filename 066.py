from itertools import count

def get_cont_frac(N: int) -> list[int]:
    # Get the regular continued fraction for sqrt(N)
    # Algorithm from https://en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend
    # 
    # Further information regarding Pell's equation's relation to convergents of sqrt(N) fractions:
    # https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
    a = int(N**0.5)
    a0 = int(N**0.5)
    m = 0
    d = 1
    seq = []
    h = [a0]
    k = [1]
    for i in count(1):
        m = d * a - m
        d = (N - m**2) / d
        a = int((a0 + m)/d)
        if len(h) == 1:
            # h2 = a1*a0 + 1 / a1
            # k2 = a1
            h.append(h[0] * a + 1)
            k.append(a)
        else:
            h.append(a*h[i - 1] + h[i - 2])
            k.append(a*k[i - 1] + k[i - 2])
        seq.append(a)
        if h[-1] ** 2 - N * k[-1] ** 2 == 1:
            # Stop at the first instance of h and k values that
            # fit the Pell's equation, indicating that it is solved
            # --> Return the minimal x-value
            return h[-1]
    return None

def main() -> str:
    # x^2 - Dy^2 = 1
    # Pell's equation: x^2 - ny^2 = 1
    # 
    # Minimized x for D (or n) is the first h / k pair
    # (used to calculate the convergents)
    # that can solve the equation.
    D = 0
    x = 0
    limit = 1000
    for i in range(2, limit):
        if i ** 0.5 % 1 == 0:
            # Ignore perfect squares; no solutions
            continue
        result = get_cont_frac(i)
        if result > x:
            D = i
            x = result
    return f"{D=}, {x=}"

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
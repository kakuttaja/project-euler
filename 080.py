
def isqrt(c: int) -> float:
    # Digit-by-digit calculation of sqrt(x)
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation
    if c ** 0.5 % 1 == 0: return 0
    p = 0
    while (p + 1)**2 <= c:
        p += 1
    digits = []
    d, r = p, c - p ** 2
    while len(digits) < 100:
        digits.append(str(d))
        d = 0
        l = r * 100
        while d * (20 * p + d) < l:
            y = d * (20 * p + d)
            if y > l:
                break
            d += 1
        d -= 1
        p = 10 * p + d
        r = l - y
    return sum(map(int, digits))

def main() -> int:
    return sum(map(isqrt, range(100)))

if __name__ == '__main__':
    print(main())
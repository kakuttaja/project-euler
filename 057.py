

def main():
    # With the convergent being p/q, the next convergent is always (p + 2q)/(p + q)!
    ans = 0
    numerator = 1
    denominator = 1
    for _ in range(1000):
        numerator, denominator = numerator + 2 * denominator, denominator + numerator
        if len(str(numerator)) > len(str(denominator)):
            ans += 1
    return ans

if __name__ == '__main__':
    print(main())

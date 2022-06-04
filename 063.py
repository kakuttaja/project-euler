

def main():
    # 10^(n-1) <= x^n < 10^n
    # Therefore lower limit is 10^[(n-1)/n]
    # and lim [(n-1)/n] = 1 when x -> infinity
    # x <= 9 always, otherwise the equation is impossible
    #
    # Therefore if the lower limit is 9 or higher,
    # a fitting x can not exist, meaning no more possible integers.
    #
    # Solving an equation for 10^(n-1)/n >= 9
    # results in n >= 21
    #
    # Therefore the upper limit of powers is 22,
    # and no more n-digit positive integers exist for nth powers.
    ans = 0
    digits = 1
    while True:
        lower_limit = 10**((digits-1)/digits)
        if lower_limit >= 9:
            return ans
        for i in range(1, 10):
            if len(str(i**digits)) == digits:
                ans += 1
        digits += 1

if __name__ == '__main__':
    print(main())

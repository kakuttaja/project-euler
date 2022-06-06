

def main():
    # Get highest number between 2/5 and 3/7
    # In a/b < 3/7 => 7a < 3b => 7a = 3b - 1
    # Therefore highest a = (3*b-1)/7,
    # which is the closest number to 3/7.
    #
    # As the numerator a must be an integer,
    # a % 1 == 0 must be checked.
    ans = 0
    b = 2
    prev = 0
    while b <= 10**6:
        a = (3*b - 1)/7
        if a/b > prev and a % 1 == 0:
            prev = a/b
            ans = int(a)
        b += 1
    return ans

if __name__ == '__main__':
    print(main())

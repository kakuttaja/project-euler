from itertools import permutations

def main():
    # Create a list of 0-9 pandigital permutations
    # Form 3-number sub-strings and check divisibility
    # With each corresponding prime
    ans = 0
    primes = [2, 3, 5, 7, 11, 13, 17]
    pandigitals = set(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    for p in pandigitals:
        if p[0] == 0: # Ignore numbers that start with 0 -> not 10-number length
            continue
        for i in range(1, 8):
            num = str(p[i]) + str(p[i+1]) + str(p[i+2])
            if int(num) % primes[i-1] != 0:
                break
            if i == 7:
                ans += int(''.join([str(i) for i in p]))
    return ans

if __name__ == '__main__':
    print(main())

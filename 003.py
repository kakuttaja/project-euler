
def prime_generator(limit):
    prime_bools = [True] * limit
    prime_bools[0] = False
    prime_bools[1] = False
    for i in range(2, len(prime_bools) - 1):
        if not prime_bools[i]:
            continue
        for j in range(i**2, len(prime_bools), i):
            prime_bools[j] = False
    return [int(i) for i, _ in enumerate(prime_bools) if prime_bools[i]]


def main():
    num = 600851475143
    primes = prime_generator(int(num**0.5))
    for p in primes:
        if num % p == 0:
            ans = p
    return ans
    

if __name__ == '__main__':
    print(main())


def prime_generator(limit: int) -> list[int]:
    primality = [True]*limit
    primality[0] = False
    primality[1] = False
    for i in range(len(primality)):
        if primality[i]:
            for j in range(i*i, len(primality), i):
                primality[j] = False
    return [int(i) for i, _ in enumerate(primality) if primality[i]]

def main():
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function#Computing_Euler%27s_totient_function
    # To maximize the ratio between the number and the totient,
    # we must minimize Euler's totient function.
    #
    # This can be effectively done by creating a number that has
    # the most small primes as possible, to minimize the (1-1/p) denominator.
    #
    # In other words, we create a number that uses all the lowest prime numbers, 
    # until it is the highest possible number below a million.
    ans = 1
    limit = 10**6
    primes = prime_generator(5000)
    i = 0
    while True:
        ans *= primes[i]
        i += 1
        if ans * primes[i] > limit:
            break
    return ans

if __name__ == '__main__':
    print(main())

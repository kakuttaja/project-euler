
def generate_primes(num):
    sieve = [True]*(num)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i*i, len(sieve), i):
                sieve[j] = False
    return [int(i) for i, _ in enumerate(sieve) if sieve[i]]

def is_prime(n: int) -> bool:
    # 6k+1 optimized prime checker copied from Wikipedia as I'm too lazy to write
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

def main():
    # Returns the first odd composite number that is
    # not possible to write as a sum of a prime and 2*square
    #
    # In the formula x = p + 2 * i^2
    # => i = sqrt[(x-p)/2]
    #
    # Due to the fact that i must be a natural number,
    # if i % 1 != 0, the prime number used to test the conjecture
    # can be entirely disregarded, as no fitting i exists
    x = 3
    primes = generate_primes(10000)
    while True:
        if not is_prime(x):
            can_be_written = False
            for p in primes:
                if p > x or (((x - p)/2)**0.5) % 1:
                    continue
                can_be_written = True
                break
            if not can_be_written:
                return x
        x += 2

if __name__ == '__main__':
    print(main())

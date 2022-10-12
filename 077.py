from eulerlib.prime_numbers import prime_gen
from itertools import count

def p2(n: int, primes: list[int]) -> int:
    # Number of partitions of n into prime parts. http://oeis.org/A000607
    # Key: power            - argument n
    # Value: coefficient    - the number of ways
    found_primes = {i: 0 for i in range(n + 1)}
    found_primes[0] = 1
    for p in primes:
        # Get all new powers of x from the prime
        new_nums = [int(i) for i in range(p, n + 1, p)]

        # Get old powers of x to calculate the sum of powers
        old_nums = [int(i) for i in found_primes.keys() if found_primes[i] > 0]

        # Taking the sum of old and new powers, taking the coefficient into account
        new_sums = [(i + j, found_primes[i]) for j in new_nums for i in old_nums if i + j < n + 1]

        # Update the dictionary with the new coefficient
        for num in new_sums:
            found_primes[num[0]] += num[1]
    return found_primes[n]

def main() -> int:
    primes_list = []
    p = prime_gen()
    for i in count(1):
        # Generate more primes as needed
        if not primes_list or max(primes_list) < i:
            for num in p:
                primes_list.append(num)
                if num > i:
                    break
        if p2(i, primes_list) >= 5000:
            return i
    return 0

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
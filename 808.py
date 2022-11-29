from eulerlib import prime_gen

def is_palindrome(s1: any) -> bool:
    return str(s1) == str(s1)[::-1]

def main() -> None:
    # Creates a list of prime squares over time
    # and checks if the reverse of a new prime square
    # is found in the list to get reversible prime squares
    # 
    # Almost certainly plenty of ways to improve efficiency.
    prime_generator = prime_gen()
    old_primes = set()
    result_primes = set()
    for p in prime_generator:
        sq = p ** 2
        if is_palindrome(sq): continue
        rsq = int(str(sq)[::-1])
        if rsq in old_primes:
            result_primes.add(sq)
            result_primes.add(rsq)
        old_primes.add(sq)
        if len(result_primes) == 50:
            break
    return sum(result_primes), len(result_primes)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
from eulerlib import primes

def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main() -> int:
    p = primes(1000000)
    s, n = 0, 0
    nums = 0
    start = 0
    while len(p) - start > nums:
        s = 0
        n = 0
        for i in range(start, len(p)):
            n += p[i]
            s += 1
            if n < 1000000 and s > nums and is_prime(n):
                nums = s
                prime = n
            elif n > 1000000:
                break
        start += 1
    return nums, prime

if __name__ == "__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
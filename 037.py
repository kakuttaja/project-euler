
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    # Primes can only end in 1, 3, 7, or 9.
    # Ending in 1 or 9 leads to non-prime numbers
    # when truncating left-to-right
    # 
    # Also these primes must consist of
    # primes smaller than them
    # i.e., must start with [2, 3, 7] and end with [3, 7]
    # 
    # Too lazy to think of a clever way to use primes already obtained
    # as PyPy takes 0.17s to complete without optimization.
    ans = set()
    i = 3
    while True:
        if is_prime(i):
            i2 = i3 = i
            if i > 10:
                while str(i2)[1:] and i3 // 10 > 0:
                    i2 = int(str(i2)[1:])
                    i3 = i3 // 10
                    if not is_prime(i2) or not is_prime(i3):
                        break
                else:
                    ans.add(i)
        if len(ans) == 11:
            break
        if i % 10 == 3:
            i += 4
        else:
            i += 6
    return sum(ans)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
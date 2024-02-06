import functools

@functools.cache
def factorial(n: int) -> int:
    if n == 1:
        return n
    return factorial(n - 1) * n

def main():
    ans = 0
    for n in range(1, 101):
        for r in range(1, n):
            if factorial(n) / (factorial(r) * factorial(n - r)) > int(1e6):
                ans += 1
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
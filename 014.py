import functools

def main() -> int:
    # Added lru_cache from functools to improve performance
    # by caching previously found values
    # 
    # Too lazy to make a dynamic dictionary for the same purpose.
    ans = 0
    length = 0

    @functools.lru_cache(None)
    def collatz(num: int) -> int:
        if num == 1: return 1
        if num % 2 == 0: num = num // 2
        else: num = 3 * num + 1
        return collatz(num) + 1
    
    for i in range(1, 10**6):
        result = collatz(i)
        if result > length:
            length = result
            ans = i
    return ans


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

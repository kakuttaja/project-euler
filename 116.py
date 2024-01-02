from time import perf_counter
import functools

@functools.cache
def rec(r: int, c: int) -> int:
    # Recursively go through a list of either
    # adding a tile or just moving on by 1.
    # Efficiency via memoization.
    if r == 0:
        return 1
    if r < 0:
        return 0
    ans = rec(r - c, c) + rec(r - 1, c)
    return ans

def main() -> None:
    color = [2, 3, 4]
    r = 50
    ans = 0
    for c in color:
        ans += rec(r, c) - 1
    return ans

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
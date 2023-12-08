from time import perf_counter
from collections import defaultdict

def main() -> int:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    cache = defaultdict(lambda: 0)
    cache[0] = 1
    for coin in coins:
        # Calculate the number of ways for each coin
        # to produce a certain number
        # e.g. 1p has exactly one way to produce every number.
        # 
        # By bottom-up solving, all numbers end up with
        # a total number of ways they can be made with
        # all the possible different coins.
        for m in range(1, 201):
            remainder = m - coin
            if remainder < 0:
                continue
            cache[m] += cache[remainder]
    return cache[200]

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 4)}s")
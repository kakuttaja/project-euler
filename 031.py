
def main() -> int:
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    target = 200
    def rec(target: int, idx: int) -> int:
        total = 0
        if idx == 7: return 1
        for i in range(idx, len(coins)):
            if target - coins[i] == 0: total += 1
            if target - coins[i] > 0: total += rec(target - coins[i], i)
        return total

    return rec(target, 0)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

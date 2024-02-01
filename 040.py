
def f(n: int) -> int:
    nums = [int(i) for i in str(n)]
    while True:
        yield nums.pop(0)
        if not nums:
            n += 1
            nums.extend([int(i) for i in str(n)])

def main():
    ans = 1
    idx = 0
    wanted = (1, 10, 100, 1000, 10000, 100000, 1000000)
    for n in f(0):
        if idx in wanted:
            wanted = wanted[1:]
            ans *= n
        idx += 1
        if not wanted:
            break
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
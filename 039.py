from collections import defaultdict

def main():
    ans = defaultdict(lambda: 0)
    for a in range(1, 1000):
        for b in range(a + 1, 1000 - a):
            c = (a ** 2 + b ** 2) ** 0.5
            if c % 1 != 0 or sum((a,b,c)) > 1000:
                continue
            c = int(c)
            ans[sum((a, b, c))] += 1
    return max(ans.keys(), key=lambda x: ans[x])

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
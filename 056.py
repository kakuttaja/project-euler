
def main():
    ans = 0
    for a in range(2, 100):
        for b in range(2, 100):
            s = sum(map(int, str(a ** b)))
            if s > ans:
                ans = s
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
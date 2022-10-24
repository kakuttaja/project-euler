
def main() -> int:
    ans = set()
    for a in range(2, 101):
        for b in range(2, 101):
            ans.add(a**b)
    return len(ans)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")

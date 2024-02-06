
def main():
    # While not eloquent, it's quite fast enough.
    ans = 0
    for i in range(10, 10000):
        steps = 0
        j = i + int(str(i)[::-1])
        while str(j) != str(j)[::-1]:
            j += int(str(j)[::-1])
            steps += 1
            if steps > 50:
                ans += 1
                break
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
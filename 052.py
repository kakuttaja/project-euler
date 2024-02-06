from itertools import count

def main():
    for i in count(60):
        s = sorted([j for j in str(i)])
        for k in range(1, 6):
            j = i * k
            if sorted([l for l in str(j)]) != s:
                break
        else:
            return i

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
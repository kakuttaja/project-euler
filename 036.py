
def main():
    return sum([i for i in range(int(1e6)) if (str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1])])

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
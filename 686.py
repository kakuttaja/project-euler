from math import log10


def main():
    # Using math formula from https://math.stackexchange.com/a/2006181
    # 
    # Updated to consider intervals between powers of 2,
    # leading to much more efficient iterating by skipping
    # numbers that can't be correct.
    # 
    # The intervals between numbers starting with 123
    # were just manually checked, seemed to hold through.
    values = 1
    target = 678910
    L = 123
    n = 1 
    k = 3
    intervals = [196, 289, 485]
    while values < target:
        for i in intervals:
            b = int(10**((n+i)*log10(2)-int(1+((n+i)*log10(2)))+k))
            if b == L:
                values += 1
                n += i
                break
        else:
            n += 1
    return n

if __name__ == '__main__':
    import time
    s = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - s, 2)}s")

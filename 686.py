from math import log10


def main():
    # Using math formula from https://math.stackexchange.com/a/2006181
    values = 0
    target = 678910
    L = 123
    n = 1 
    k = 3
    while True:
        b = int(10**(n*log10(2)-int(1+(n*log10(2)))+k))
        if b == L:
            values += 1
            if values == target:
                return n
        n += 1

if __name__ == '__main__':
    import time
    s = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - s, 2)}s")
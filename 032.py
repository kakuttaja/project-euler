
def pan(n: str) -> bool:
    return all(n.count(i) == 1 and i != '0' for i in n)

def main():
    # Bad but extremely simple and good enough, I suppose.
    lim = int(1e4)
    found = set()
    for a in range(1, 1000):
        if not pan(str(a)): continue
        for b in range(1234 // a, lim // a + 1):
            if not pan(str(b)): continue
            cs = str(a) + str(b) + str(a * b)
            if len(cs) == 9 and pan(cs):
                found.add(a * b)
    return sum(found)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
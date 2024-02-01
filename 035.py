
def get_primes(lim: int) -> list:
    p = [True] * lim
    p[0] = False
    p[1] = False
    for i in range(lim):
        if p[i]:
            for j in range(i + i, lim, i):
                p[j] = False
    return [int(i) for i, b in enumerate(p) if b]

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    primes = get_primes(int(1e6))
    ans = set()
    for p in primes:
        if p in ans:
            continue
        rotations = [p]
        origin = [str(i) for i in str(p)]
        plist = [str(i) for i in str(p)]
        plist.insert(0, plist.pop())
        while plist != origin:
            n = int(''.join(plist))
            if not is_prime(n):
                break
            rotations.append(n)
            plist.insert(0, plist.pop())
        else:
            if all(is_prime(n) for n in rotations):
                for n in rotations:
                    ans.add(n)
    return len(ans)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
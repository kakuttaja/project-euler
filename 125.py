
def is_palindrome(n):
    rev = 0
    t = n
    while t != 0:
        rev = (rev * 10) + (t % 10)
        t = t // 10
    return rev == n

def main():
    LIM = 100_000_000
    p = set()

    start = 1

    while start * start < LIM:
        nsum = start * start

        end = start + 1
        while True:
            nsum += end * end

            if nsum >= LIM:
                break

            if is_palindrome(nsum):
                p.add(nsum)
            end += 1

        start += 1
    return sum(p)

if __name__ == '__main__':
    from time import perf_counter_ns
    start = perf_counter_ns()
    print(main())
    print(f"This took {round((perf_counter_ns() - start) / 1e6, 1)}ms")
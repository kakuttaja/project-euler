

def get_next_chain(n: int) -> int:
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    num = 0
    for m in str(n):
        num += factorials[int(m)]
    return num

def factorial_chains(n: int) -> int:
    chain = [n]
    steps = 0
    while True:
        steps += 1
        n = get_next_chain(n)
        if n in chain:
            return steps
        chain.append(n)

def main():
    ans = 0
    i = 1
    for i in range(1, 10**6):
        num = factorial_chains(i)
        if num == 60:
            ans += 1
    return ans

if __name__ == '__main__':
    import time
    start = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - start, 2)}s")

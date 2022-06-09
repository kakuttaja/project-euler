from math import log10

def f(n):
    ans = 0
    k = int(log10(n)) +1
    for i in range(k):
        d = (n % 10**(i+1)) - (n % 10**i)
        d /= (10**i)
        ans += d
    return int(ans)

def main():
    # Not ordered, have to solve more than 30 numbers
    # and take the 30th number from the set, hoping for the best..
    # 
    # limit = 33 was manually determined to be the lowest limit
    # that still returns the same number as limit > 100..
    i = 2
    limit = 33
    nums = set()
    while len(nums) < limit:
        n = i
        j = 2
        while j < 50:
            n *= i
            if f(n) == i:
                nums.add(n)
            if len(nums) == limit:
                break
            j += 1
        i += 1
    return sorted(list(nums))[29]

if __name__ == '__main__':
    import time
    start = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - start, 2)}s")

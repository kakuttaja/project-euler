
def main():
    # Numbers must be in order,
    # the shortest possible code includes each number once
    # 
    # Easily implemented in a form of a sorting algorithm
    # that compares indices of numbers against the expected order
    passes = set()
    nums = set()
    with open("079.txt") as f:
        for line in f.readlines():
            line = line.strip().split()[0]
            t = tuple(map(int, line))
            for n in t: nums.add(n)
            for i in range(len(t) - 1):
                for j in range(i + 1, len(t)):
                    passes.add((t[i], t[j]))
    nums = list(nums)
    while True:
        changed = False
        for (a, b) in passes:
            x, y = nums.index(a), nums.index(b)
            if x > y:
                nums[x], nums[y] = nums[y], nums[x]
                changed = True
        if not changed:
            break
    return ''.join(map(str, nums))

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
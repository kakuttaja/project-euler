from itertools import count

def main():
    ans = 0
    for i in count(1):
        nums = str(i)
        if any([nums.count(i) > 1 for i in nums]):
            continue
        # n > 1, therefore if our number concatenated
        # with n = 2 is too high, we've reached the limit
        if len(nums + str(i * 2)) > 9:
            break
        j = 2
        while True:
            nums += str(i * j)
            j += 1
            if len(nums) >= 9:
                break
        if len(nums) == 9 and all([nums.count(i) == 1 for i in "123456789"]):
            if int(nums) > ans:
                ans = int(nums)
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
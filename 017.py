
def lens(nums: list) -> int:
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    t = ""
    for i in range(len(nums)):
        n = nums[i]
        if i == 0 and ones[n]:
            t += f"{ones[n]}hundred"
            if sum(nums[i + 1:]) > 0:
                t += "and"
        elif i == 1:
            if n == 1 and nums[i + 1] > 0:
                t += teens[nums[i + 1]]
                break
            t += tens[n]
        else:
            t += ones[n]
    return len(t)

def letters(n: int) -> int:
    if n == 1000:
        return 11
    nums = []
    while n > 0:
        n0 = n % 10
        nums.insert(0, n0)
        n //= 10
    while len(nums) < 3:
        nums.insert(0, 0)
    return lens(nums)

def main():
    return sum(map(letters, range(1, 1000 + 1)))

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")


def generate_products():
    nums = set()
    for i in range(100, 1000):
        for j in range(100, 1000):
            nums.add(i * j)
    return list(nums)

def main():
    ans = 0
    nums = generate_products()
    for n in nums:
        if str(n) == str(n)[::-1] and n > ans:
            ans = n
    return ans

if __name__ == '__main__':
    print(main())


def check_digits(numbers: list[int]):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            break
    else: return 1
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] < numbers[i + 1]:
            break
    else: return -1
    return 0

def main():
    limit = 0.99
    bouncy = 0
    n = 100
    ratio = bouncy / n
    while ratio < limit:
        if check_digits([int(i) for i in str(n)]) == 0:
            bouncy += 1
        ratio = bouncy / n
        n += 1
    return n-1

if __name__ == '__main__':
    import time
    s = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - s, 2)}s")



RESULTS = {}

def collatz(num: int):
    i = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3*num + 1
        if num in RESULTS.keys():
            return RESULTS[num] + i
        i += 1
    return i

def main():
    ans = 0
    num = 0
    for i in range(1, 1*10**6):
        n = collatz(i)
        if i not in RESULTS.keys():
            RESULTS[i] = n
        if n > ans:
            num = i
            ans = n
    return num

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main", number=10))
    print(main())
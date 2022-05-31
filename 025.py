

def main():
    # The period of the repeating sequences in numbers 
    # is the smallest power of 10 that is divisible by (denominator - 1)
    # In other words, 10**period % j == 1
    ans = 0
    best = 0
    for i in range(1, 1000):
        for j in range(1, i):
            if 10**j % i == 1:
                if j > best:
                    best = j
                    ans = i
                break
    return ans, best

if __name__ == '__main__':
    print(main())

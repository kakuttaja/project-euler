

def main():
    ans = 0
    primes = [True] * 2*10**6
    for i in range(2, len(primes)):
        if primes[i]:
            ans += i
            for j in range(i * i, len(primes), i):
                primes[j] = False
    return ans

if __name__ == '__main__':
    print(main())
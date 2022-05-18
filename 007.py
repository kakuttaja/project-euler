
class NotPrime(Exception): pass

def main():
    primes = [2]
    num = 3
    target = 10001
    while True:
        if num % 2 == 0:
            num += 1
            continue
        try:
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    raise NotPrime
        except NotPrime:
            num += 1
            continue
        primes.append(num)
        if len(primes) == target:
            return num
        num += 1


if __name__ == '__main__':
    print(main())
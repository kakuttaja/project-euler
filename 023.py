

def get_abundancy(n) -> bool:
    divs = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divs += i
            if divs > n: return True
    return False

def main():
    # Every integer greater than 20161 can be written as a sum
    abundants = set()
    for i in range(1, 20162):
        if i in abundants:
            continue
        if get_abundancy(i):
            for j in range(1, 20162 // i + 1):
                abundants.add(i * j)
    
    sums = set()
    for n in abundants:
        for m in abundants:
            sums.add(n + m)
    return sum([int(i) for i in range(1, 20162) if i not in sums])


if __name__ == '__main__':
    print(main())

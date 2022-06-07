from math import log10


def load_numbers():
    numbers = []
    idx = 0
    with open("099_numbers.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            idx += 1
            a, b = line.replace("\n", "").split(",")
            numbers.append((idx, int(a), int(b)))
    return numbers

def main():
    ans = 0
    highest = 0
    numbers = load_numbers()
    for line, base, exp in numbers:
        num = exp*log10(base)
        if num > highest:
            highest = num
            ans = line
    return ans

if __name__ == '__main__':
    print(main())

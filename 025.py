from math import log10

def main():
    a, b = 0, 1
    idx = 1
    digits = 1000
    while True:
        a, b = b, a + b
        if int(log10(a)+1) == digits:
            return idx
        idx += 1

if __name__ == '__main__':
    print(main())

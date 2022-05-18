

def fibgen():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield b

def main():
    ans = 0
    for n in fibgen():
        if n > 4 * 10**6:
            return ans
        if n % 2 == 0:
            ans += n

if __name__ == '__main__':
    print(main())
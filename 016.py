

def main():
    num = 2 ** 1000
    return sum([int(i) for i in str(num)])


if __name__ == '__main__':
    print(main())

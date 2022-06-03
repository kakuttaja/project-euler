

def main():
    # Generate triangle numbers and check
    # if these numbers are also pentagonal and hexagonal numbers
    i = 286
    while True:
        x = i*(i+1)/2
        if (((24*(x) + 1)**0.5 + 1) / 6) % 1 == 0 and (1+(8*x+1)**0.5)/4 % 1 == 0:
            return int(x)
        i += 1

if __name__ == '__main__':
    print(main())

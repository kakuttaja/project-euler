

def main():
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(101):
        sum_of_squares += i**2
        square_of_sum += i
    return square_of_sum**2 - sum_of_squares 

if __name__ == '__main__':
    print(main())


def main():
    # Upper limit is the highest 1_2_3_4_5_6_7_8_9_0 number
    # while the lower limit is the lowest.
    #
    # Returns the first (only) number that matches
    # the given pattern mathematically.
    # 
    # The variable i has to end in 0, for the square to also
    # end with the number 0, therefore += 10 loops.
    upper = int(1929394959697989990**0.5)
    lower = int(1020304050607080900**0.5)
    nums = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1] # Reverse order for while-loop
    i = lower
    while i <= upper:
        x = i**2
        num_index = 0
        while x > 0:
            num = x % 10
            if num != nums[num_index]:
                break
            num_index += 1
            x = x // 100
        else:
            return i
        i += 10
    return 0

if __name__ == '__main__':
    import time
    start = time.time()
    print(main())
    print(f"Time taken: {round(time.time() - start, 2)}s")



def get_cipher():
    with open("059_cipher.txt", "r", encoding="utf-8") as f:
        text = f.read().split(",")
    return text

def main():
    # This function forms a best-guess for each
    # possible letter in the encryption key (n=3)
    # by counting the amount of letters
    # that a guessed encryption key leads to after xor.
    cipher = [int(i) for i in get_cipher()]
    probable_letters = {}

    for start_index in range(3):
        most_letters = 0
        for i in range(97, 123):
            temp_sum = 0
            idx = 0
            letters = 0
            while idx + start_index < len(cipher):
                temp_sum += cipher[idx+start_index]^i
                if 97 <= (cipher[idx+start_index]^i) < 123:
                    letters += 1
                idx += 3
            if letters > most_letters:
                most_letters = letters
                probable_letters[start_index] = temp_sum
    return sum(probable_letters.values())

if __name__ == '__main__':
    print(main())

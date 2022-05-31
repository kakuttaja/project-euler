

def triangle_generator(limit=50):
    triangles = []
    for i in range(1, limit+1):
        triangles.append(int(0.5 * i * (i + 1)))
    return triangles


def main():
    ans = 0
    triangles = triangle_generator()
    alphabet = [str(i) for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    with open("042_words.txt", "r", encoding="utf-8") as f:
        for word in f.read().replace('"', "").split(","):
            if word == "SKY":
                a = 0
            word_value = 0
            for letter in word:
                word_value += alphabet.index(letter) + 1
            if word_value in triangles:
                ans += 1
    return ans

if __name__ == '__main__':
    print(main())

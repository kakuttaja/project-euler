

def load_names() -> list:
    with open("022_names.txt", "r", encoding="utf-8") as f:
        ret = [str(i) for i in f.read().replace('"', "").split(",")]
    return sorted(ret)

def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    names = load_names()
    ans = 0
    for idx, name in enumerate(names):
        for letter in name:
            ans += (alphabet.find(letter) + 1) * (idx + 1)
    return ans


if __name__ == '__main__':
    print(main())

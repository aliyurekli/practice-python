# File Overlap


def read_to_list(file):
    a = []

    with open(file, "r") as f:
        data = f.readlines()
        for line in data:
            num = int(line.strip())
            a.append(num)

    return a


if __name__ == '__main__':
    a1 = read_to_list("data/happynumbers.txt")
    a2 = read_to_list("data/primenumbers.txt")

    print(set(a1) & set(a2))

# Draw a Game Board


def print_horizontal(n):
    print((" ---" * n).rstrip())


def print_vertical(n):
    print(("|   " * (n + 1)).rstrip())


def draw_board(n):
    for i in range(n+1):
        print_horizontal(n)

        if i != n:
            print_vertical(n)


if __name__ == '__main__':
    size = int(input("What will be the size of the board? "))

    draw_board(size)

# Tic Tac Draw


def pretty_print(grid):
    for i in range(3):
        print("%d\t%d\t%d" % (grid[i][0], grid[i][1], grid[i][2]))


def initialize_matrix():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def mark_grid(grid, x, y, num):
    if grid[x][y] == 0:
        grid[x][y] = num
        return True
    else:
        return False


def check_grid(grid):

    for x in range(0, 3):
        row = {grid[x][0], grid[x][1], grid[x][2]}
        if len(row) == 1 and grid[x][0] != 0:
            print("Player %d wins" % grid[x][0])
            return True

    for x in range(0, 3):
        column = {grid[0][x], grid[1][x], grid[2][x]}
        if len(column) == 1 and grid[0][x] != 0:
            print("Player %d wins" % grid[0][x])
            return True

    diagonal1 = {grid[0][0], grid[1][1], grid[2][2]}

    if len(diagonal1) == 1 and grid[0][0] != 0:
        print("Player %d wins" % grid[0][0])
        return True

    diagonal2 = {grid[0][2], grid[1][1], grid[2][0]}

    if len(diagonal2) == 1 and grid[1][1] != 0:
        print("Player %d wins" % grid[1][1])
        return True

    return False


def count_empty_cells(grid):
    count = 0

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                count += 1

    return count


def check_user_input(u1, u2):
    inputs = [0, 1, 2]

    return u1 in inputs and u2 in inputs

# Check Tic Tac Toe

import random


def generate_row():
    return [random.randint(0, 2) for j in range(3)]


def check_grid(grid):
    conditions = []

    for x in range(0, 3):
        row = {grid[x][0], grid[x][1], grid[x][2]}
        if len(row) == 1 and grid[x][0] != 0:
            conditions.append("Player %d has a winning condition" % grid[x][0])

    for x in range(0, 3):
        column = {grid[0][x], grid[1][x], grid[2][x]}
        if len(column) == 1 and grid[0][x] != 0:
            conditions.append("Player %d has a winning condition" % grid[0][x])

    diagonal1 = {grid[0][0], grid[1][1], grid[2][2]}

    if len(diagonal1) == 1 and grid[0][0] != 0:
        conditions.append("Player %d has a winning condition" % grid[0][0])

    diagonal2 = {grid[0][2], grid[1][1], grid[2][0]}

    if len(diagonal2) == 1 and grid[1][1] != 0:
        conditions.append("Player %d has a winning condition" % grid[1][1])

    return conditions


if __name__ == '__main__':

    matrix = []

    for i in range(3):
        matrix.append(generate_row())

    print(matrix)

    result = check_grid(matrix)

    if len(result) == 0:
        print("There is no winner")
    else:
        for condition in result:
            print(condition)

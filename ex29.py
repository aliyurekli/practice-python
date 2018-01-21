# Tic Tac Toe Game

import ex27


if __name__ == '__main__':

    matrix = ex27.initialize_matrix()

    while True:

        # Player 1 turn
        if ex27.count_empty_cells(matrix) == 0:
            print("Draw, no winner.")
            break
        else:
            ex27.pretty_print(matrix)

        while True:
            p1_x = int(input("Player 1, mark x position (0,1,2):"))
            p1_y = int(input("Player 1, mark y position (0,1,2):"))

            if ex27.check_user_input(p1_x, p1_y):
                if ex27.mark_grid(matrix, p1_x, p1_y, 1):
                    break
                else:
                    print("Player 1, please choose empty positions.")
            else:
                print("Player 1, please re-enter positions (0,1,2)")

        if ex27.check_grid(matrix):
            ex27.pretty_print(matrix)
            break

        # Player 2 Turn
        if ex27.count_empty_cells(matrix) == 0:
            break
        else:
            ex27.pretty_print(matrix)

        while True:
            p2_x = int(input("Player 2, mark x position (0,1,2):"))
            p2_y = int(input("Player 2, mark y position (0,1,2):"))

            if ex27.check_user_input(p2_x, p2_y):
                if ex27.mark_grid(matrix, p2_x, p2_y, 2):
                    break
                else:
                    print("Player 2, please choose empty positions.")
            else:
                print("Player 2, please re-enter positions (0,1,2).")

        if ex27.check_grid(matrix):
            ex27.pretty_print(matrix)
            break

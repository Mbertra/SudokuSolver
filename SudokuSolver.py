import random

row = 0
col = 0


# this is a method using backtracking algorithm to solve a sudoku board recursively
def solve_sudoku(sudoku_board):
    search_empty = find_location(sudoku_board)

    # find an empty spot on the board or return finished
    if not search_empty:
        return True
    else:
        row, col = search_empty
    for num in range(1, 10):
        if is_safe(sudoku_board, num, row, col):
            sudoku_board[row][col] = num

            if solve_sudoku(sudoku_board):
                return True

            sudoku_board[row][col] = 0

    return False


def print_board(board):
    for rows in board:
        print(rows)


# generates a random board, using the same method as solving, except with random.
# we don't use this for solving because it's slower time complexity
def generate_board(sudoku_board):
    search_empty = find_location(sudoku_board)

    # find an empty spot on the board or return finished
    if not search_empty:
        return True
    else:
        row, col = search_empty
    for num in range(1, 10):
        num = random.randint(1, 9)
        if is_safe(sudoku_board, num, row, col):
            sudoku_board[row][col] = num

            if solve_sudoku(sudoku_board):
                return True

            sudoku_board[row][col] = 0

    return False


# fills in 50% of the board with 0's
def fill_zeros(board):
    for i in range(9):
        for j in range(9):
            if random.randint(0, 1) == 1:
                board[i][j] = 0
    return board


# this will check if the number we want to assign is already in our 3x3 square
def used_in_square(board, num, row, col):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return True
    return False


# this searches for a location if there are any that need solved
def find_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return False


# this will check if the number we want to assign is used in its col
def used_in_col(board, num, col):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False


# this will check if the number we want to assign is used in its row
def used_in_row(board, num, row):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False


# checks if the number we are trying to place works with the rules of sudoku
def is_safe(board, num, row, col):
    if not used_in_square(board, num, row - row % 3, col - col % 3):
        if not used_in_row(board, num, row):
            if not used_in_col(board, num, col):
                return True
    return False

# creates a board of 0's to initialize, solves a board using random numbers
# and then fills the board with some 0's to make it a playable board
def create_playable():
    # initialize a board of 0's
    sudoku_board = [[0 for i in range(9)] for j in range(9)]
    generate_board(sudoku_board)
    fill_zeros(sudoku_board)

    return sudoku_board


def main():
    # makes a playable random board
    print("Generated Board")
    board = create_playable()
    print_board(board)

    print("Solved board")
    solve_sudoku(board)
    print_board(board)


if __name__ == '__main__':
    main()

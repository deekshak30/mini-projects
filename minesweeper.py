def create_board(rows, cols):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    return board


def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * (4 * len(row) - 1))

def place_mines(board, num_mines):
    import random

    rows = len(board)
    cols = len(board[0])

    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1
def count_adjacent_mines(board):
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] != '*':
                count = 0
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        if board[x][y] == '*':
                            count += 1
                board[i][j] = str(count)

def play_game(rows, cols, num_mines):
    board = create_board(rows, cols)
    place_mines(board, num_mines)
    count_adjacent_mines(board)
    print_board(board)

# Play the Minesweeper game
rows = 5
cols = 5
num_mines = 5

play_game(rows, cols, num_mines)

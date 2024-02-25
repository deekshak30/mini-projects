
board = [[' ' for _ in range(3)] for _ in range(3)]
def print_board():
    for row in board:
        print(' | '.join(row))
        print('-' * 9)
def check_win():
    
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

   
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def play_game():
    player = 'X'
    turns = 0

    while turns < 9:
        print_board()

        row = int(input("Enter the row number (0-2): "))
        col = int(input("Enter the column number (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            turns += 1

            if check_win():
                print_board()
                print(f"Player {player} wins!")
                break

            player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is already taken. Try again.")

    if turns == 9:
        print_board()
        print("It's a tie!")


play_game()



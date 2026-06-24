# Tic Tac Toe

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def display_board():
    print()
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("--+---+--")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("--+---+--")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()


def player_input(player):
    while True:
        row = int(input("Player " + player + ", enter row 1-3: "))
        col = int(input("Player " + player + ", enter column 1-3: "))

        row = row - 1
        col = col - 1

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Try again.")
        elif board[row][col] != " ":
            print("This place is already taken. Try again.")
        else:
            board[row][col] = player
            break


def check_win(player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def check_tie():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def play():
    current_player = "X"

    while True:
        display_board()
        player_input(current_player)

        if check_win(current_player):
            display_board()
            print("Player " + current_player + " wins!")
            break

        if check_tie():
            display_board()
            print("It's a tie!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


play()
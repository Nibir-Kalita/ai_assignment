
board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("------")

def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

def minimax(is_max):
    result = check_winner()

    if result == "X":
        return 1
    if result == "O":
        return -1
    if result == "Draw":
        return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def computer_move():
    best_score = float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(True)
            board[i] = " "

            if score < best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "O"

while True:
    print_board()

    if check_winner():
        break

    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move >= 9 or board[move] != " ":
        print("Invalid move")
        continue

    board[move] = "X"

    if check_winner():
        break

    computer_move()

print_board()
print("Result:", check_winner())


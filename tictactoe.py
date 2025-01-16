import math

# Function to display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if there is a winner
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm for AI decision making
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # Computer wins
        return 1
    if winner == "X":  # User wins
        return -1
    if is_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

# Function to find the best move for the computer
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    display_board(board)

    while True:
        # User move
        while True:
            try:
                user_move = input("Enter your move (row and column, e.g., 1 1): ")
                row, col = map(int, user_move.split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers (0-2).")

        display_board(board)

        # Check if user wins
        if check_winner(board) == "X":
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Computer move
        print("Computer's turn...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
        display_board(board)

        # Check if computer wins
        if check_winner(board) == "O":
            print("The computer wins. Better luck next time!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
tic_tac_toe()

import pprint


def isSafe(board, x, y, n):
    # Checking whether the column is filled
    for row in range(x):
        if board[row][y] == "Q":
            return False

    # Checking for top left diagonals are filled
    row = x
    col = y
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False

        row -= 1
        col -= 1

    # Checking for top right diagonals are filled
    row = x
    col = y
    while row >= 0 and col < n:
        if board[row][col] == "Q":
            return False
        row -= 1
        col += 1

    return True


def nQueen(board, x, n):
    # if we have successfully placed n queens return True
    if x >= n:
        return True
    # iterate through columns for each row
    for col in range(n):
        # if the particular position is safe then place that queen
        if isSafe(board, x, col, n):
            board[x][col] = "Q"
            # if the next queen cannot be placed then backtrack
            if nQueen(board, x + 1, n):
                return True

            board[x][col] = " "
    return False


n = int(input("Enter number of Q "))
board = [[" "] * n for i in range(n)]
if nQueen(board, 0, n):
    pprint.pprint(board)
else:
    print("No Solution")

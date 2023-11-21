class NQBacktracking:

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Function to print Chessboard
    def printSolution(self, board):
        print()
        print("N Queen Backtracking Solution: ")
        print(f"Initial Position    (x: {self.x}, y: {self.y})")
        print()
        for line in board:
            print(line)

    # Function to check if a square is attacked or not
    def is_attack(self, i, j, board):
        for k in range(0, N):
            if board[i][k] == 1 or board[k][j] == 1:
                return True
        for k in range(0, N):
            for l in range(0, N):
                if (k+l == i+j) or (k-l == i-j):
                    if board[k][l] == 1:
                        return True
        return False

    # Function to solve N Queen
    def solveNQ(self):
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[self.x][self.y] = 1

        if not self.solveNQUtil(board, 0):
            print()
            print("Solution does not exist")
            print()
            return False

        self.printSolution(board)
        return True

    # Utility function for solveNQ (recursive backt utility fn)
    def solveNQUtil(self, board, col):

        if col >= N:
            return True

        if col == self.y:
            return self.solveNQUtil(board, col + 1)

        for i in range(N):
            if i == self.x:
                continue
            if (not (self.is_attack(i, col, board))) and (board[i][col] != 1):
                board[i][col] = 1
                if self.solveNQUtil(board, col + 1):
                    return True
                board[i][col] = 0

        return False


N = int(input("Enter the size of the board (N): "))

# Get the initial position (x, y) from the user
x = int(input("Enter the initial row: "))
y = int(input("Enter the initial column: "))

NQBt = NQBacktracking(x, y)
NQBt.solveNQ()

# ----------------------------------------------------------------------

# OUTPUT- (where solution exists)

# Enter the size of the board (N): 4
# Enter the initial row: 2
# Enter the initial column: 0

# N Queen Backtracking Solution:
# Initial Position    (x: 2, y: 0)

# [0, 1, 0, 0]
# [0, 0, 0, 1]
# [1, 0, 0, 0]
# [0, 0, 1, 0]

# ----------------------------------------------------------------------

# OUTPUT- (where solution does not exists)

# Enter the size of the board (N): 4
# Enter the initial row: 0
# Enter the initial column: 0

# Solution does not exist

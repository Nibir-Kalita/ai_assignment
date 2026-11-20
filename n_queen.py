
def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solve(0)

    for solution in solutions:
        for i in range(n):
            print(" ".join("Q" if solution[i] == j else "." for j in range(n)))
        print()

    print("Total solutions:", len(solutions))


n = int(input("Enter number of queens: "))
solve_n_queens(n)


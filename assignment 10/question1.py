# Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
# according to the following constraints.
# a. Each row should have exactly only one queen.
# b. Each column should have exactly only one queen.
# c. No queens are attacking each other.
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row=0, board=None, solutions=None):
    if board is None:
        board = [-1] * n
    if solutions is None:
        solutions = []

    if row == n:
        solutions.append(board[:])
        return solutions

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)
            board[row] = -1

    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print("".join("Q" if i == row else "#" for i in range(len(solution))))
        print("\n")

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"Number of solutions: {len(solutions)}")
    print_solutions(solutions)
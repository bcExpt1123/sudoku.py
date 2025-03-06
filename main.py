import generate_sudoku from problem_generator
import solve_sudoku from solver

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    sudoku_board = generate_sudoku()
    print_board(sudoku_board)
    print("-------------------------------------------------")
    solve_sudoku(sudoku_board)
    print_board(sudoku_board)

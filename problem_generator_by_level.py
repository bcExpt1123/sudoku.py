import random
import argparse

def generate_sudoku(difficulty="medium"):
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, side + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    difficulty_levels = {
        "easy": 0.4,   # 40% of the board will be empty
        "medium": 0.55, # 55% of the board will be empty
        "hard": 0.7     # 70% of the board will be empty
    }

    empties = int(side * side * difficulty_levels.get(difficulty, 0.55))
    for p in random.sample(range(side * side), empties):
        board[p // side][p % side] = 0

    return board

def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Sudoku puzzle with a given difficulty level.")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium", help="Set the difficulty level of the Sudoku puzzle.")
    args = parser.parse_args()

    sudoku_board = generate_sudoku(args.difficulty)
    print_sudoku(sudoku_board)

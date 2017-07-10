"""A solution to the sudoku checker in codewars."""


def valid_solution(board):
    """Check if Sudoku Board input is a win. Takes in a list of lists."""
    from collections import Counter
    hold = []
    transpose = []
    for x in range(len(board)):
        for k, i in Counter(board[x]).items():
            if i > 1 or k is 0:
                return False
        column = [[row[i] for row in board] for i in range(len(board))]
        for x in range(len(column)):
            for k, i in Counter(column[x]).items():
                if i > 1 or k is 0:
                    return False
        for y in range(0, 7, 3):
            for x in range(0, 10, 3):
                if len(hold) > 8:
                    transpose.append(hold)
                    hold = []
                if len(hold) < 9:
                    hold.extend(board[y][x:x + 3])
                    hold.extend(board[y + 1][x:x + 3])
                    hold.extend(board[y + 2][x:x + 3])
        for x in range(len(transpose)):
            for k, i in Counter(transpose[x]).items():
                if i > 1 or k is 0:
                    return False
    return True

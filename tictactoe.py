"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Count the number of X's and O's on the board
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    # X always goes first, so the turn alternates based on counts
    return 'X' if x_count == o_count else 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    possibleAction = set()
    for i in range(len(board)) :
        for j in range(len(board[i])):
            if  board[i][j] == EMPTY:
                possibleAction.add(i, j)
    return possibleAction



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    deep_board = copy.deepcopy(board)
    # Validate the action
    if action not in actions(board):
        raise ValueError("Invalid action")

    # Get the current player
    current_player = player(board)

    # Apply the move
    i, j = action
    deep_board[i][j] = current_player

    return deep_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    # Check horizontal wins
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY:
            return row[0]

    # Check vertical wins
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != EMPTY:
            return check[0]

    # Check diagonal wins (top-left to bottom-right)
    diagonal1 = [board[i][i] for i in range(len(board))]
    if diagonal1.count(diagonal1[0]) == len(diagonal1) and diagonal1[0] != EMPTY:
        return diagonal1[0]

    # Check diagonal wins (top-right to bottom-left)
    diagonal2 = [board[i][len(board) - i - 1] for i in range(len(board))]
    if diagonal2.count(diagonal2[0]) == len(diagonal2) and diagonal2[0] != EMPTY:
        return diagonal2[0]

    # If no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    
    return winner(board) or all(cell != EMPTY for row in board for cell in row)
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

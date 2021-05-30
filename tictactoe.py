"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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

    # Counting no. of occurance of X and O in board
    count_X = 0
    count_O = 0
    for row in board:
        count_X += row.count(X)
        count_O += row.count(O)

    # If empty board or no. of X < no. of O it's X's turn
    if count_X == count_O:
        return X
    
    # If no. of X > no. of O than it's O's turn
    if count_X > count_O:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy of the board(don't change the original board)
    copy = deepcopy(board)
    i = action[0]
    j = action[1]
    # If the current action is invalid
    if copy[i][j] != EMPTY:
        raise Exception("Invalid move")

    # Result board
    copy[i][j] = player(copy)

    return copy    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Searching for winner row-wise
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # Searching column-wise
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == X:
                countX += 1
            elif board[j][i] == O:
                countO += 1
        if countX == 3:
            return X
        elif countO == 3:
            return O
        else:
            countX = 0
            countO = 0
    
    # Searching Diagonally
    dig = [[board[0][0], board[1][1], board[2][2]],
           [board[0][2], board[1][1], board[2][0]]]
    for row in dig:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # End of funtion, no winner
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If the board is completely filled
    empty = 0
    for row in board:
        empty += row.count(EMPTY)
    if empty == 0:
        return True
    
    # If there is a winner
    if winner(board):
        return True

    # End of the function, game still on!
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Actions available on the board
    actionSet = actions(board)

    # Dictionary for storing each action's board value
    values = {}

    # Storing the current board's player
    Player = player(board)
    for action in actionSet:
        # Calls value function to calculate each resulting board's value
        values[action] = value(result(board, action))

        # Applying alpha-beta pruning
        if Player is X and  values[action] == 1:
            return action
        elif Player is O and values[action] == -1:
            return action

    # See who's turn it is in order to return the optimal solution
    if Player is X:
        return max(values, key=values.get)
    else:
        return min(values, key=values.get)

def value(board):
    """
    Returns the value of a board
    """
    # Base case
    if terminal(board):
        return utility(board)

    # Not terminal case, strive for the optimal solution
    return value(result(board, minimax(board)))
    


    

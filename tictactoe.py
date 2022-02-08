"""
Tic Tac Toe Player
"""

import math
import copy
from socket import errorTab
from xml.dom.minidom import Element

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
    xCounter = 0
    oCounter = 0
    for horizontalOrder in board :
        for verticalOrder in horizontalOrder :
            if verticalOrder == O:
                oCounter += 1
            elif verticalOrder == X:
                xCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    for i, horizontalOrder in enumerate(board):
        for j, verticalOrder in enumerate(horizontalOrder):
            if verticalOrder == EMPTY:
                possibleActions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] != EMPTY) and (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
            if (board[i][0] == X):
                return X
            else:
                return O
        
        if (board[0][i] != EMPTY) and (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]):
            if (board[0][i] == X):
                return X
            else:
                return O

    """outta for-loop for non-horizontal-vertical"""
    if (board[0][0] != EMPTY) and (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        if (board[0][0] == X):
            return X
        else:
            return O
    if (board[0][2] != EMPTY) and (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        if (board[0][2] == X):
            return X
        else:
            return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


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

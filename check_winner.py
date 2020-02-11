#!/usr/bin/env python3

def check_all_cases(board):
    values = []
    values.append(player_1_first_row(board))
    values.append(player_1_second_row(board))
    values.append(player_1_third_row(board))
    values.append(player_1_first_col(board))
    values.append(player_1_second_col(board))
    values.append(player_1_third_col(board))
    values.append(player_1_left_diag(board))
    values.append(player_1_right_diag(board))
    values.append(player_2_first_row(board))
    values.append(player_2_second_row(board))
    values.append(player_2_third_row(board))
    values.append(player_2_first_col(board))
    values.append(player_2_second_col(board))
    values.append(player_2_third_col(board))
    values.append(player_2_left_diag(board))
    values.append(player_2_right_diag(board))
    for v in values:
        if v != 0:
            return v

def player_1_first_row(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return 1
    else:
        return 0

def player_1_second_row(board):
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return 1
    else:
        return 0

def player_1_third_row(board):
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return 1
    else:
        return 0

def player_1_first_col(board):
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return 1
    else:
        return 0

def player_1_second_col(board):
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return 1
    else:
        return 0

def player_1_third_col(board):
    if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return 1
    else:
        return 0

def player_1_left_diag(board):
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 1
    else:
        return 0

def player_1_right_diag(board):
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 1
    else:
        return 0

def player_2_first_row(board):
    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return 2
    else:
        return 0

def player_2_second_row(board):
    if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return 2
    else:
        return 0

def player_2_third_row(board):
    if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return 2
    else:
        return 0

def player_2_first_col(board):
    if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return 2
    else:
        return 0

def player_2_second_col(board):
    if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return 2
    else:
        return 0

def player_2_third_col(board):
    if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return 2
    else:
        return 0

def player_2_left_diag(board):
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return 2
    else:
        return 0

def player_2_right_diag(board):
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return 2
    else:
        return 0

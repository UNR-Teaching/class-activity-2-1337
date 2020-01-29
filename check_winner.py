#!/usr/bin/env python3


class CheckWinner(object):

    def check_all_cases(self, board):
        values = []
        values.append(self.player_1_first_row(board))
        values.append(self.player_1_second_row(board))
        values.append(self.player_1_third_row(board))
        values.append(self.player_1_first_col(board))
        values.append(self.player_1_second_col(board))
        values.append(self.player_1_third_col(board))
        values.append(self.player_1_left_diag(board))
        values.append(self.player_1_right_diag(board))
        values.append(self.player_2_first_row(board))
        values.append(self.player_2_second_row(board))
        values.append(self.player_2_third_row(board))
        values.append(self.player_2_first_col(board))
        values.append(self.player_2_second_col(board))
        values.append(self.player_2_third_col(board))
        values.append(self.player_2_left_diag(board))
        values.append(self.player_2_right_diag(board))
        for v in values:
            if v != 0:
                return v

    def player_1_first_row(self, board):
        if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
            return 1
        else:
            return 0

    def player_1_second_row(self, board):
        if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
            return 1
        else:
            return 0

    def player_1_third_row(self, board):
        if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
            return 1
        else:
            return 0

    def player_1_first_col(self, board):
        if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
            return 1
        else:
            return 0

    def player_1_second_col(self, board):
        if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
            return 1
        else:
            return 0

    def player_1_third_col(self, board):
        if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
            return 1
        else:
            return 0

    def player_1_left_diag(self, board):
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return 1
        else:
            return 0

    def player_1_right_diag(self, board):
        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            return 1
        else:
            return 0

    def player_2_first_row(self, board):
        if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
            return 2
        else:
            return 0

    def player_2_second_row(self, board):
        if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
            return 2
        else:
            return 0

    def player_2_third_row(self, board):
        if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
            return 2
        else:
            return 0

    def player_2_first_col(self, board):
        if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
            return 2
        else:
            return 0

    def player_2_second_col(self, board):
        if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
            return 2
        else:
            return 0

    def player_2_third_col(self, board):
        if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
            return 2
        else:
            return 0

    def player_2_left_diag(self, board):
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return 2
        else:
            return 0

    def player_2_right_diag(self, board):
        if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            return 2
        else:
            return 0

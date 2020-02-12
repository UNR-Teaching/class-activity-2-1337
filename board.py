#!/usr/bin/env python3
from check_winner import check_all_cases


class Board(object):
    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]

    def mark_square(self, move):
        """
        Marks a square at coordinate (column, row) for player

        :param move: (tuple:(int,int,str)) column, row, player

        :return: ????
        """
        column = move[0]
        row = move[1]
        player = move[2].upper()
        if self.board[row][column] is not '_':
            return self.board

        self.board[row][column] = player
        return self.board

    def has_winner(self):
        return check_all_cases(self.board)

    def print_board(self):
        for pos in self.board:
            print(f"{pos[0]}\t{pos[1]}\t{pos[2]}")

    def recv_move(self, move, player_id):
        move = self.parse_move(move)
        if move == -1:
            return move
        else:
            return self.mark_square(move)

    def parse_move(self, move):
        moveArr = move.split(',')
        if len(moveArr) != 3:
            return -1
        if len(moveArr[0]) != 1 and len(moveArr[1]) != 1 and len(moveArr[2]):
            return -1
        if moveArr[0].isnumeric() is False or int(moveArr[0]) > 3 or int(moveArr[0]) < 0:
            return -1
        if moveArr[1].isnumeric() is False or int(moveArr[1]) > 3 or int(moveArr[1]) < 0:
            return -1
        if moveArr[2].upper() != "X" and moveArr[2].upper() != 'O':
            return -1

        return int(moveArr[0]), int(moveArr[1]), moveArr[2].upper()

    def check_cats_game(self):
        c = 0
        for i in range(0, 2):
            for j in range(0, 2):
                if self.board[i][j] == '_':
                    c += 1
        if c != 0:
            return False
        else:
            return True

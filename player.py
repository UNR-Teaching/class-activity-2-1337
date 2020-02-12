#!/usr/bin/env python3


class Player:
    def __init__(self, id):
        self.id = id

    def send_move(self, board, move):
        valid = board.recv_move(move, self.id)
        return valid

    def get_move(self, board):
        valid = -1
        while valid != -1:
            move = input(f"Player {self.id} enter a move (col, row, player): ")
            self.send_move(board, move)

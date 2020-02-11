#!/usr/bin/env python3


class Player:
    def __init__(self, id):
        self.id = id
    def send_move(self,board,move):
        valid = board.parse_move(move)
        return valid
    def get_move(self):
        valid = False
        while valid != True:
            move = input(f"Player {self.id} enter a move: ")
            self.send_move(move)

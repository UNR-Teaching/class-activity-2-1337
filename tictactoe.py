#!/usr/bin/env python3
from check_winner import CheckWinner
""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming,
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
        self.over = False
        self.winner = CheckWinner()
        pass

    def mark_square(self, move):
        """
        Marks a square at coordinate (column, row) for player

        :param move: (tuple:(int,int,str)) column, row, player

        :return: ????
        """
        print(move)
        column = move[0]
        row = move[1]
        player = move[2].upper()

        self.board[row][column] = player
        return self.board

    def has_winner(self):
        print(f'Winner: {self.winner.check_all_cases(self.board)}')
        return self.winner.check_all_cases(self.board)

    def print_board(self):
        for pos in self.board:
            print(f"{pos[0]}\t{pos[1]}\t{pos[2]}")

    def parse_move(self,move):
        moveArr = move.split(',')
        print(moveArr)
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

        return (int(moveArr[0]), int(moveArr[1]), moveArr[2].upper())

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """
        while self.over is False:
            move = input("Input a move(column, row, player): ")
            valid_move=self.parse_move(move)
            if valid_move == -1:
                print("Invalid move!")
                continue
            self.mark_square(valid_move)
            self.print_board()
            if self.has_winner() == 1:
                return 1
            elif self.has_winner() == 2:
                return 2

        pass


if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    if winner == 1 or winner == 2:
        print(f"{winner} has won!")
    else:
        print("Cat's game, no one wins")

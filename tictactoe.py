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
        player = move[2].upper()
        column = move[0]
        row = move[1]

        if column > 3 or row > 3:
            print("Not a valid position!")
            return 1
        if player != "X" and player != 'O':
            print("Invalid player!")
            return 1

        self.board[row][column] = player
        return 0

    def has_winner(self):
        print(f'Winner: {self.winner.check_all_cases(self.board)}')
        return self.winner.check_all_cases(self.board)

    def print_board(self):
        for pos in self.board:
            print(f"{pos[0]}\t{pos[1]}\t{pos[2]}")

    def getMove(self):
        move = input("Input a move(column, row, player): ")
        moveArr = move.split(',')
        if len(moveArr) != 3:
            print("Invalid move")
            return 1
        if len(moveArr[0]) != 1 and len(moveArr[1]) != 1 and len(moveArr[2]):
            print("Invalid move")
            return 1
        if moveArr[0].isnumeric() is False and int(moveArr[0]) > 3:
            print("Invalid column")
            return 1
        if moveArr[1].isnumeric() is False and int(moveArr[0]) > 3:
            print("Invalid row")
            return 1

        print(moveArr)
        return int(moveArr[0]), int(moveArr[1]), moveArr[2]

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """
        while self.over is False:
            move = self.getMove()
            if move == -1:
                continue
            self.mark_square(move)
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

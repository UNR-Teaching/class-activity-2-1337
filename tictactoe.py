#!/usr/bin/env python3
""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming,
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_','_','_'],

                      ['_','_','_'],
                      ['_','_','_']]
        self.over = False

        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        player = player.upper()
        if column > 3 or row > 3:
            print("Not a valid position!")
            return 1
        if player is not "X" or player is not "O":
            print("Invalid player!")
            return 1

        self.board[row][column] = player
        return 0

        pass

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """

        pass
    def print_board(self):


    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """
        while self.over is False:
            move = input("Input a move(column, row, player): ")
            moveArr = move.split(',')
            mark_square(moveArr[0],moveArr[1],moveArr[2])

        pass

if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print(f"{winner} has won!")

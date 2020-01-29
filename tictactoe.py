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

    def mark_square(self, move):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        column = move[0]
        row = move[1]
        player = move[2].upper()

        self.board[row][column] = player
        return self.board

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        # Check if player 1 has won on horizontals
        if board[0][0:2] == 'X' or board[1][0:2] == 'X' or board[2][0:2] == 'X':
            return 1
        # Check if player 1 has won on verticals
        if board[0:2][0] == 'X' or board[0:2][1] == 'X' or board[0:2][2] == 'X':
            return 1
        # Check if player 2 has won on horizontals:
        if board[0][0:2] == 'O' or board[1][0:2] == 'O' or board[2][0:2] == 'O':
            return 2
        # Check if player 1 has won on verticals
        if board[0:2][0] == 'O' or board[0:2][1] == 'O' or board[0:2][2] == 'O':
            return 2

    def print_board(self):
        for pos in self.board:
            print(f"{pos[0]}\t{pos[1]}\t{pos[2]}")

    def parse_move(self,move):
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

        pass

if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print(f"{winner} has won!")

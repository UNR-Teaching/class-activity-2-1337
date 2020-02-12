#!/usr/bin/env python3


class Game(object):
    def __init__(self, board, p1, p2):
        self.board = board
        self.p1 = p1
        self.p2 = p2
        self.over = False

    def check_over(self):
        """
        Checks if the game is over
        :return: the id of the winning player
        """
        if self.board.has_winner() == 1:
            return 1
        elif self.board.has_winner() == 2:
            return 2
        elif self.board.check_cats_game():
            return 0
        else:
            return -1

    def play_game(self):
        """
            Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

            :return: (str) the letter representing the player who won
        """
        while self.over is False:
            self.board.print_board()
            winner = self.check_over()
            if winner != -1:
                return winner
            self.p1.get_move(self.board)
            self.board.print_board()
            winner = self.check_over()
            if winner != -1:
                return winner
            self.p2.get_move(self.board)


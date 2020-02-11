#!/usr/bin/env python3


class Game(object):
    def __init__(self, board, p1, p2):
        self.board = board
        self.p1 = p1
        self.p2 = p2

    def play_game(self):
        """
            Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

            :return: (str) the letter representing the player who won
        """
        while self.over is False:
            move = input("Input a move(column, row, player): ")
            valid_move = self.parse_move(move)
            if valid_move == -1:
                print("Invalid move!")
                continue
            self.mark_square(valid_move)
            self.print_board()
            self.check_cats_game()
            if self.has_winner() == 1:
                return 1
            elif self.has_winner() == 2:
                return 2


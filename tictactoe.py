#!/usr/bin/env python3
from board import Board
from player import Player
from game import Game
""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming,
          and you make use of relevant object-oriented design principles.
"""


def main():
    player1 = Player(1)
    player2 = Player(2)
    board = Board()
    game = Game(board, player1, player2)
    winner = game.play_game()
    if winner == 1 or winner == 2:
        print(f"Player {winner} has won!")
    else:
        print("Cat's game, no one wins")


if __name__ == '__main__':
    main()

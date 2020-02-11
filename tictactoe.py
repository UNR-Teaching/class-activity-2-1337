#!/usr/bin/env python3
from board import Board
""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming,
          and you make use of relevant object-oriented design principles.
"""

def main():


if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    if winner == 1 or winner == 2:
        print(f"Player {winner} has won!")
    else:
        print("Cat's game, no one wins")

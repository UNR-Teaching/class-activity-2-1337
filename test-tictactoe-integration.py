#!/usr/bin/env python3
import unittest
from tictactoe import *
from check_winner import *


class TestTicTacToeIntegration(unittest.TestCase):

    def test_game_player1_win(self):
        player1 = Player(1)
        player2 = Player(2)
        board = Board()
        game = Game(board, player1, player2)
        player1.send_move(board, '0,0,X')
        player2.send_move(board, '0,1,0')
        player1.send_move(board, '1,1,X')
        player2.send_move(board, '0,2,O')
        player1.send_move(board, '2,2,X')
        winner = game.check_over()
        self.assertEqual(1, winner)

    def test_game_player2_win(self):
        player1 = Player(1)
        player2 = Player(2)
        board = Board()
        game = Game(board, player1, player2)
        player1.send_move(board, '1,0,X')
        player2.send_move(board, '0,1,O')
        player1.send_move(board, '1,1,X')
        player2.send_move(board, '0,2,O')
        player1.send_move(board, '2,2,X')
        player2.send_move(board, '0,0,O')
        winner = game.check_over()
        self.assertEqual(2, winner)

    def test_game_cats_game(self):
        player1 = Player(1)
        player2 = Player(2)
        board = Board()
        game = Game(board, player1, player2)
        player1.send_move(board, '0,0,X')
        player2.send_move(board, '1,0,O')
        player1.send_move(board, '2,0,X')
        player2.send_move(board, '0,1,O')
        player1.send_move(board, '1,1,X')
        player2.send_move(board, '2,1,O')
        player1.send_move(board, '1,2,X')
        player2.send_move(board, '0,2,O')
        player2.send_move(board, '2,2,O')
        winner = game.check_over()
        self.assertEqual(0, winner)




if __name__ == '__main__':
    unittest.main()

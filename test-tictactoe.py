#!/usr/bin/env python3

import unittest
from tictactoe import *

class Test(unittest.TestCase):

    def test_parseMove_lower_player(self):
        board = Board()
        self.assertEqual(board.parse_move('1,1,x'), (1,1,'X'))
        self.assertEqual(board.parse_move('1,1,o'), (1,1,'O'))
    def test_parseMove_upper_player(self):
        board = Board()
        self.assertEqual(board.parse_move('1,1,X'), (1,1,'X'))
        self.assertEqual(board.parse_move('1,1,O'), (1,1,'O'))
    def test_parseMove_ivalid_position(self):
        board = Board()
        self.assertTrue(board.parse_move('1,e,o') is -1)
        self.assertTrue(board.parse_move('e,1,o') is -1)
    def test_parseMove_outside_board(self):
        board = Board()
        self.assertTrue(board.parse_move('-1,-1,x') is -1)
        self.assertTrue(board.parse_move('4,4,x') is -1)

    def test_mark_square(self):
        board = Board()
        self.assertEqual(board.mark_square((1,1,'X')),[['_','_','_'],['_','X','_'],['_','_','_']])
        board = Board()
        self.assertEqual(board.mark_square((0,0,'O')),[['O','_','_'],['_','_','_'],['_','_','_']])
        board = Board()
        self.assertEqual(board.mark_square((2,2,'X')),[['_','_','_'],['_','_','_'],['_','_','X']])

    def test_overwire_test(self):
        board = Board()
        self.assertEqual(board.mark_square((0,0,'X')),[['X','_','_'],['_','_','_'],['_','_','_']])
        self.assertEqual(board.mark_square((0,0,'O')),[['X','_','_'],['_','_','_'],['_','_','_']])

if __name__ == '__main__':
    unittest.main()

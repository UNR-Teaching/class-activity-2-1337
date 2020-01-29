#!/usr/bin/env python3

import unittest
from tictactoe import *

class Test(unittest.TestCase):

    def test_parseMove(self):
        board = Board()
        self.assertEqual(board.parse_move('1,1,x'), (1,1,'X'))
        self.assertEqual(board.parse_move('1,1,o'), (1,1,'O'))
        self.assertEqual(board.parse_move('1,e,o'), -1)
        self.assertEqual(board.parse_move('1,1,e'), -1)
        self.assertEqual(board.parse_move('-1,-1,x'), -1)
        self.assertEqual(board.parse_move('4,4,x'), -1)

    def test_mark_square(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

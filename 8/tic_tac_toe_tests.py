import unittest
from minimax import find_best_move
from tic_tac_toe import TicTacToePiece, TicTacToeBoard

class TicTacToeMinimaxTestCase(unittest.TestCase):
    def test_easy_position(self):
        # Win in 1 move
        to_win_easy_position = [TicTacToePiece.X, TicTacToePiece.O, TicTacToePiece.X,
                                TicTacToePiece.X, TicTacToePiece.E, TicTacToePiece.O,
                                TicTacToePiece.E, TicTacToePiece.E, TicTacToePiece.O]
        test_board = TicTacToeBoard(to_win_easy_position, TicTacToePiece.X)
        answer = find_best_move(test_board)
        self.assertEqual(answer, 6)

    def test_block_position(self):
        # Must block O's win
        to_block_position = [TicTacToePiece.X, TicTacToePiece.E, TicTacToePiece.E,
                             TicTacToePiece.E, TicTacToePiece.E, TicTacToePiece.O,
                             TicTacToePiece.E, TicTacToePiece.X, TicTacToePiece.O]
        test_board = TicTacToeBoard(to_block_position, TicTacToePiece.X)
        answer = find_best_move(test_board)
        self.assertEqual(answer, 2)

    def test_hard_position(self):
        # Find the best move to win 2 moves
        to_win_hard_position = [TicTacToePiece.X, TicTacToePiece.E, TicTacToePiece.E,
                                TicTacToePiece.E, TicTacToePiece.E, TicTacToePiece.O,
                                TicTacToePiece.O, TicTacToePiece.X, TicTacToePiece.E]
        test_board = TicTacToeBoard(to_win_hard_position, TicTacToePiece.X)
        answer = find_best_move(test_board)
        self.assertEqual(answer, 1)


if __name__ == '__main__':
    unittest.main()

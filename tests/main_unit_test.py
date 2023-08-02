from unittest.mock import patch
from io import StringIO
import unittest

from main import get_valid_bid, get_challenge_input, ai_make_bid, liar_dice_game

class TestLiarDiceGame(unittest.TestCase):
    def test_get_valid_bid(self):
        with patch('builtins.input', side_effect=['3 4', '2 3']):
            self.assertEqual(get_valid_bid((3, 4)), (2, 3))

    def test_get_challenge_input(self):
        with patch('builtins.input', side_effect=['y']):
            self.assertTrue(get_challenge_input())
        with patch('builtins.input', side_effect=['n']):
            self.assertFalse(get_challenge_input())

    def test_ai_make_bid(self):
        current_bid = (3, 4)
        bid = ai_make_bid(current_bid)
        self.assertTrue(1 <= bid[0] <= 6)
        self.assertTrue(current_bid[1] + 1 <= bid[1] <= current_bid[1] + 3)

    @patch('builtins.input', side_effect=['2', '5', '3', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_liar_dice_game(self, mock_stdout, mock_input):
        liar_dice_game()
        self.assertIn("Player 1's turn", mock_stdout.getvalue())
        self.assertIn("Player 2's turn", mock_stdout.getvalue())
        self.assertIn("Round 1", mock_stdout.getvalue())
        self.assertIn("Round 2", mock_stdout.getvalue())
        self.assertIn("Round 3", mock_stdout.getvalue())
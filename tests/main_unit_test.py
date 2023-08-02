import unittest
from unittest.mock import patch
from io import StringIO
from main import roll_dice, valid_bid, challenge, liar_dice_game

class TestLiarDiceGame(unittest.TestCase):
    def test_roll_dice(self):
        self.assertEqual(len(roll_dice(5)), 5)
        self.assertTrue(all(1 <= die <= 6 for die in roll_dice(5)))

    def test_valid_bid(self):
        self.assertTrue(valid_bid((3, 4), (2, 3)))
        self.assertFalse(valid_bid((2, 3), (3, 4)))
        self.assertFalse(valid_bid((3, 3), (3, 2)))

    def test_challenge(self):
        self.assertTrue(challenge((4, 5), {1: 1, 2: 2, 3: 1, 4: 0, 5: 1, 6: 1}))
        self.assertFalse(challenge((3, 4), {1: 1, 2: 2, 3: 1, 4: 0, 5: 1, 6: 1}))
        self.assertFalse(challenge((2, 3), {1: 1, 2: 2, 3: 1, 4: 0, 5: 1, 6: 1}))

    @patch('builtins.input', side_effect=['3 4', '2 3', '4 5', '1 6', '5 3', '6 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_liar_dice_game(self, mock_stdout, mock_input):
        liar_dice_game(2, 5, 3)
        self.assertIn("Player 1's turn", mock_stdout.getvalue())
        self.assertIn("Player 2's turn", mock_stdout.getvalue())
        self.assertIn("Round 1", mock_stdout.getvalue())
        self.assertIn("Round 2", mock_stdout.getvalue())
        self.assertIn("Round 3", mock_stdout.getvalue())
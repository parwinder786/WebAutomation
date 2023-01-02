import unittest
import randomGameFunction
class TestGame(unittest.TestCase):
    def test_input(self):
        ans = 5
        guess = 5
        result = randomGameFunction.run_guess(ans, guess)
        self.assertTrue(result)

    def test_input_wrong(self):
        ans = 4
        guess = 5
        result = randomGameFunction.run_guess(ans, guess)
        self.assertFalse(result)

    def test_input_incorrect(self):
        ans = 4
        guess = 11  #it is greater than 10
        result = randomGameFunction.run_guess(ans, guess)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        ans = 4
        guess = '12'  # it is string than int
        result = randomGameFunction.run_guess(ans, guess)
        self.assertFalse(result)

if __name__ == '__main__':    unittest.main()


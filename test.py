#importing our app.py file so that we can use functions
from main import odds_sum,has_letter_cases,find_lowercase_vowel
import unittest

class TestMain(unittest.TestCase):
    def test_odds_sum(self):
        self.assertEqual(odds_sum([1, 2, 3]),4, "Should be 4")

    def test_has_letter_cases(self):
        self.assertEqual(has_letter_cases("abcDEF"),True, "Should be True")

    def test_find_lowercase_vowel(self):
        self.assertEqual(find_lowercase_vowel("cats"),1, "Should be 1")

if __name__ == '__main__':
    unittest.main()


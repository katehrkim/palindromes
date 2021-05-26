# Can you translate this driver code to unit tests?
import unittest
from palindrome import palindrome
# This should return a bunch of trues
class PalindromeTestCase(unittest.TestCase):
    """Tests for palindrome.py"""
    def test_one(self):
        self.assertEqual(palindrome('racecar'), True)
    def test_two(self):
        self.assertEqual(palindrome('Noon'), True)
    def test_three(self):
        self.assertEqual(palindrome('ciVic'), True)
    def test_four(self):
        self.assertEqual(palindrome('nice'), False)
    def test_five(self):
        self.assertEqual(palindrome(434), True)
    def test_six(self):
        self.assertEqual(palindrome(123), False)
    def test_seven(self):
        self.assertEqual(palindrome('bomb'), False)
    # The following should be True if you're trying to do the extra portion of this challenge
    def test_eight(self):
        self.assertEqual(palindrome('Sore was I ere I saw Eros.'), True)
    def test_nine(self):
        self.assertEqual(palindrome('A man, a plan, a canal -- Panama'), True)

    if __name__ == '__main__':
        unittest.main()

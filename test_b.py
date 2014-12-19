import unittest
import b
import nltk

class TestB(unittest.TestCase):
    def setUp(self):
        print nltk.util.unicode_literals

    def tearDown(self):
        print "rab"

    def test_b_fn(self):
        self.assertEqual(4, b.fn(2))

if __name__ == "__main__":
    unittest.main()

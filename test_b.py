import unittest
import b
from nltk.stem import WordNetLemmatizer

class TestB(unittest.TestCase):
    def setUp(self):
        wnl = WordNetLemmatizer()
        print wnl.lemmatize('dogs')

    def tearDown(self):
        print "rab"

    def test_b_fn(self):
        self.assertEqual(4, b.fn(2))

if __name__ == "__main__":
    unittest.main()

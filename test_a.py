import unittest
import a

class TestA(unittest.TestCase):
    def setUp(self):
        print "foo"

    def tearDown(self):
        print "bar"

    def test_a_one(self):
        self.assertEqual(2, a.fn(2))

if __name__ == "__main__":
    unittest.main()

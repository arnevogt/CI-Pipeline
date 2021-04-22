import unittest

from src.tools import add


class Test_Tools(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,4), 9)

if __name__ == '__main__':
    unittest.main()

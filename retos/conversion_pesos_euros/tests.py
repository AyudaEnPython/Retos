"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import peso_a_euro


class Test(unittest.TestCase):

    def test_peso_a_euro(self):
        self.assertEqual(peso_a_euro(10_000), 2.2222222222222223)
        self.assertEqual(peso_a_euro(50_000), 11.11111111111111)


if __name__ == '__main__':
    unittest.main()

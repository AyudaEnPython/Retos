"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import solve


class Test(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(
            solve("fcdcba"),
            ["cdc"],
        )


if __name__ == "__main__":
    unittest.main()

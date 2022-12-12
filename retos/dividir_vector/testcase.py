"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import sol


class Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            sol(
                [
                    5, -8, 9, 12, 0,
                    4, -1, 25, 3, 10,
                    6, 2, 15, 7, 11,
                    5, 26, 31, 0, 4,
                ],
                20, 5,
            ),
            "-8 9 12 0 5 -1 25 3 10 4 2 15 7 11 6 26 31 0 4 5",
        )


if __name__ == "__main__":
    unittest.main()

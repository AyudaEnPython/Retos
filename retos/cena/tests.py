"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from datetime import timedelta

from main import sol, _to_str


class Test(unittest.TestCase):

    times = "05:00", "13:37", "00:10"
    expected = "04:55:00", "13:23:23", "00:09:50"

    def test_to_str(self):
        td = timedelta(hours=1, minutes=15, seconds=3)
        self.assertEqual(_to_str(td), "01:15:03")

    def test_sol(self):
        for time, expected in zip(self.times, self.expected):
            self.assertEqual(sol(time), expected)


if __name__ == "__main__":
    unittest.main()

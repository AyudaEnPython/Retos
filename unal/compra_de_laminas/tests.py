"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import json
import unittest
from main import sol


class Test(unittest.TestCase):

    input_ = (
        json.loads(
            '{"d": 55, "o": 57, "p": 65, "t": 55,' \
            '"s": 73, "f": 89, "e": 72, "k": 65, "y": 65}'
        ),
        "g q h t w p y f"
    )

    def test_sol(self):
        self.assertEqual(
            sol(*self.input_),
            ("274", "t p y f"),
        )


if __name__ == "__main__":
    unittest.main()

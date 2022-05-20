"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import json
import unittest
from main import sol


class Test(unittest.TestCase):

    inputs = (
        (
            json.loads(
            '{"d": 55, "o": 57, "p": 65, "t": 55,' \
            '"s": 73, "f": 89, "e": 72, "k": 65, "y": 65}'
            ),
            "g q h t w p y f",
        ),
        (
            json.loads(
            '{"t": 66, "u": 72, "d": 90, "r": 84,' \
            '"j": 36, "g": 50, "s": 94, "q": 62, "f": 35}'
            ),
            "d p h u i t q",
        )
    )
    outputs = (
        ("274", "t p y f"),
        ("290", "d u t q"),
    )

    def test_sol(self):
        for inp, out in zip(self.inputs, self.outputs):
            with self.subTest(inp=inp, out=out):
                self.assertEqual(sol(*inp), out)


if __name__ == "__main__":
    unittest.main()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import es_palindromo, validate, sol


class Test(unittest.TestCase):

    def test_validate(self):
        self.assertEqual(validate("*WXT+"), "*WXT+")
        self.assertEqual(validate("-*Y.$"), "-*Y.$")

    def test_sol_defaults(self):
        self.assertEqual(
            sol("*WXT+", "-*Y.$"),
            ("¥♞¥¥ØØØ¥ØØØØ¥ØØØØ¥ØØ¥Ø¥¥Ø", 4),
        )

    def test_es_palindromo(self):
        self.assertEqual(es_palindromo("Ají traga la lagartija"), True)


if __name__ == "__main__":
    unittest.main()

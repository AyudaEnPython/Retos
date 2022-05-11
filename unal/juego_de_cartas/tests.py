"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import sol, _after, _before


class Test(unittest.TestCase):

    inputs = "z,z,Z,Z,i,a,z,Z,A,A,z,a,z,A,A"
    outputs = " Z I A Z A Z A Z A \n 4 1 1 2 2 1 1 1 2 "

    def test_before(self):
        self.assertEqual(_before(self.inputs), "ZZZZIAZZAAZAZAA")
        self.assertEqual(_before("a,a,B,B,b,c,C"), "AABBBCC")

    def test_after(self):
        r = "ZIAZAZAZA"
        c = "411221112"
        self.assertEqual(_after((r, c)), self.outputs)
        self.assertEqual(_after(("ABC", "123")), " A B C \n 1 2 3 ")

    def test_sol(self):
        self.assertEqual(
            _after(sol(_before(self.inputs))),
            self.outputs,
        )


if __name__ == "__main__":
    unittest.main()

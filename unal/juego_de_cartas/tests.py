"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import sol, _after, _before


class Test(unittest.TestCase):

    inputs = (
        "z,z,Z,Z,i,a,z,Z,A,A,z,a,z,A,A",
        "A,A,a,c,g,c,B,A,F,f,b,f,E,b,f,b",
        "E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E",
    )
    inputs_after = (
        "ZZZZIAZZAAZAZAA",
        "AAACGCBAFFBFEBFB",
    )
    outputs = (
        " Z I A Z A Z A Z A \n 4 1 1 2 2 1 1 1 2 ",
        " A C G C B A F B F E B F B \n 3 1 1 1 1 1 2 1 1 1 1 1 1 ",
        " E D E D C E B E A E A E G E G E F E \n 5 1 2 1 2 2 1 2 1 1 1 1 1 1 1 1 1 1 ",
    )

    def test_before(self):
        for input_, input_after in zip(self.inputs, self.inputs_after):
            self.assertEqual(
                _before(input_),
                input_after,
            )
        self.assertEqual(_before("a,a,B,B,b,c,C"), "AABBBCC")

    def test_after(self):
        r = "ZIAZAZAZA"
        c = "411221112"
        self.assertEqual(_after((r, c)), " Z I A Z A Z A Z A \n 4 1 1 2 2 1 1 1 2 ")
        self.assertEqual(_after(("ABC", "123")), " A B C \n 1 2 3 ")

    def test_sol(self):
        for input_, output in zip(self.inputs, self.outputs):
            self.assertEqual(
                _after(sol(_before(input_))),
                output,
            )


if __name__ == "__main__":
    unittest.main()

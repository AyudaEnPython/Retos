"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import sol, P, Q


class Test(unittest.TestCase):

    cases = (
        "ABC123 DEF456 GHI789",
        "IAN373 PPP555 RRR777 BBB333 ZZZ999",
        "ONE111 TWO222 SIX666 TEN010",
    )

    def test_sol(self):
        self.assertEqual(
            sol(self.cases),
            "\n".join([P, Q, P]),
        )


if __name__ == "__main__":
    unittest.main()

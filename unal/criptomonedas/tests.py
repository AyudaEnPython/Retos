"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import sol_1, sol_2


class Test(unittest.TestCase):

    data = {
        "SOL": 50, "BTC": 29000, "DOT": 0.2,
        "SHIBA": 0.03548, "LUNA": 2, "APE": 35,
    }
    inputs = (
        "BTC SHIBA BNB APE BUSD",
        "SOL LUNA APE ",
    )
    outputs = (
        ("BTC SHIBA APE", 29035.03548),
        ("SOL LUNA APE", 87),
    )

    def test_sol(self):
        for input_, output in zip(self.inputs, self.outputs):
            self.assertEqual(
                sol_1(self.data, input_),
                output,
            )
            self.assertEqual(
                sol_2(self.data, input_),
                output,
            )


if __name__ == "__main__":
    unittest.main()

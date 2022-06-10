"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import io
import unittest
from unittest.mock import patch

from main import _table, sol, output, _percentage, _min_max, get_data


class Test(unittest.TestCase):

    n_inputs = [137, 233, 904], [552, 561, 993, 308, 249], [530, 457, 491, 470]
    m_inputs = (
        [
            [1, 148, 96],
            [2, 105, 88],
            [3, 148, 95],
            [2, 118, 84],
            [2, 134, 90],
        ],
        [
            [4, 164, 104],
            [4, 164, 106],
            [4, 84, 34],
            [3, 187, 113],
            [5, 156, 107],
            [5, 200, 155],
            [1, 141, 97],
            [4, 167, 105],
        ],
        [
            [3, 165, 38],
            [3, 173, 121],
            [1, 137, 99],
            [2, 145, 106],
            [1, 167, 120],
            [1, 130, 119],
        ]
    )
    outputs = (
        "1 127\n3 894\n1 7.30%\n2 0.00%\n3 1.11%\n",
        "5 189\n3 973\n1 1.81%\n2 0.00%\n3 2.01%\n4 14.61%\n5 24.10%\n",
        "2 457\n1 530\n1 0.00%\n2 0.00%\n3 4.07%\n4 0.00%\n",
    )
    internal_ds = (
        ([127, 233, 894], {1: 10, 2: 0, 3: 10}),
        ([542, 561, 973, 263, 189], {1: 10, 2: 0, 3: 20, 4: 45, 5: 60}),
        ([530, 457, 471, 470], {1: 0, 2: 0, 3: 20, 4: 0}),
    )
    
    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, function=None):
        if function:
            function()
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch(
        "builtins.input", 
        side_effect=(
            "3 5", "137", "233", "904",
            "1 148 96", "2 105 88", "3 148 95", "2 118 84", "2 134 90",
        )
    )
    def test_get_data(self, mocked_input):
        response = get_data()
        self.assertEqual(response, (self.n_inputs[0], self.m_inputs[0]))

    def test_table(self):
        self.assertEqual(_table(80, 60), 15)
        self.assertEqual(_table(91, 88), 0)
        self.assertEqual(_table(135, 92), 0)
        self.assertEqual(_table(145, 98), 10)
        self.assertEqual(_table(155, 108), 10)
        self.assertEqual(_table(174, 113), 20)
        self.assertEqual(_table(200, 121), 50)
        self.assertEqual(_table(200, 90), 20)

    def test_percentege(self):
        self.assertEqual(_percentage(200, 100), 50.00)

    def test_min_max(self):
        self.assertEqual(_min_max([1, 2, 3, 4, 5]), ((0, 1), (4, 5)))

    def test_sol(self):
        for i, n in enumerate(self.n_inputs):
            t, m = sol(n, self.m_inputs[i])
            self.assertEqual(t, self.internal_ds[i][0])
            self.assertEqual(m, self.internal_ds[i][1])

    def test_output(self):
        for i, (t, m) in enumerate(self.internal_ds):
            self.assert_stdout(
                self.outputs[i],
                function=lambda: output(self.n_inputs[i], t, m),
            )


if __name__ == "__main__":
    unittest.main()

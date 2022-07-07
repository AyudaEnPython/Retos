"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import io
import unittest
from unittest.mock import patch
from textwrap import dedent

from main import (
    FILENAME,
    _validate_dna,
    _validate_n,
    get_data,
    clean_up,
    sol,
    sorted_,
    show,
)


class Test(unittest.TestCase):
    inputs = (
        [
            "AACATGAAGG",
            "TTTTGGCCAA",
            "TTTGGCCAAA",
            "GATCAGATTT",
            "CCCGGGGGGA",
            "ATCGATGCAT",
        ],
    )
    outpus = (
    dedent("""\
        CCCGGGGGGA
        AACATGAAGG
        GATCAGATTT
        ATCGATGCAT
        TTTTGGCCAA
        TTTGGCCAAA
    """),
    )

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, function=None):
        if function:
            function()
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_validate_dna(self):
        self.assertEqual(_validate_dna("CCCGGGGGA"), "CCCGGGGGA")

    def test_validate_dna_error(self):
        with self.assertRaises(ValueError):
            _validate_dna("")
        
        with self.assertRaises(ValueError):
            _validate_dna("CCCGGGGGAZ")
    
    def test_validate_n(self):
        self.assertEqual(_validate_n("3", 1, 50), 3)
        self.assertEqual(_validate_n("15", 1, 50), 15)

    def test_validate_n_error(self):
        with self.assertRaises(ValueError):
            _validate_n("", 1, 50)
        with self.assertRaises(ValueError):
            _validate_n("0", 1, 50)
        with self.assertRaises(ValueError):
            _validate_n("51", 1, 50)
        with self.assertRaises(ValueError):
            _validate_n("-1", 1, 50)
        with self.assertRaises(ValueError):
            _validate_n("a", 1, 50)
        with self.assertRaises(ValueError):
            _validate_n("1.5", 1, 50)

    def test_get_data(self):
        values, data = get_data(FILENAME)
        self.assertEqual(values, ("1", "8 10", "6"))
        self.assertEqual(len(data), 1)

    def test_get_data_error(self):
        with self.assertRaises(FileNotFoundError):
            get_data("")
        with self.assertRaises(FileNotFoundError):
            get_data("DNA.dat")

    def test_clean_up(self):
        values, data = get_data(FILENAME)
        n, data = clean_up(data, values)
        cases, xy, q = values
        self.assertEqual(cases, "1")
        self.assertEqual(xy, "8 10")
        self.assertEqual(q, "6")
        self.assertEqual(data[0], self.inputs[0])
    
    def test_sol(self):
        self.assertEqual(sol("DAABEC"), ("DAABEC", 5))
        self.assertEqual(sol("AACEDGG"), ("AACEDGG", 1))
        self.assertEqual(sol("ZWQM"), ("ZWQM", 6))

    def test_sorted_(self):
        data = ["DAABEC", "AACEDGG", "ZWQM"]
        self.assertEqual(
            sorted_(data),
            [('AACEDGG', 1), ('DAABEC', 5), ('ZWQM', 6)],
        )

    def test_show(self):
        data = [
            ('CCCGGGGGGA', 9),
            ('AACATGAAGG', 10),
            ('GATCAGATTT', 11),
            ('ATCGATGCAT', 17),
            ('TTTTGGCCAA', 36),
            ('TTTGGCCAAA', 37),
        ]
        self.assert_stdout(self.outpus[0], function=lambda: show(data))


if __name__ == "__main__":
    unittest.main()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import copy
import io
import unittest
from unittest.mock import patch

from main import (
    _actions,
    get_data,
    productos,
    add,
    delete,
    update,
    _statistics,
    output
)


class Test(unittest.TestCase):

    cases = (
        ("AGREGAR", [11, "Melon", 70, 13]),
        ("BORRAR", [10, "Jamon", 15000, 10]),
        ("ACTUALIZAR", [7, "Helado", 65000, 11]),
    )
    outputs = (
        "Jamon Melon 4460.9 1015010.0\n",
        "Arandanos Galletas 3777.8 864100.0\n",
        "Helado Galletas 10950.0 1544600.0\n",
    )

    def setUp(self) -> None:
        self._products = copy.deepcopy(productos)
    
    def tearDown(self) -> None:
        pass

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, function=None):
        if function:
            function()
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_actions(self):
        self.assertEqual(_actions("AGREGAR"), add)
        self.assertEqual(_actions("BORRAR"), delete)
        self.assertEqual(_actions("ACTUALIZAR"), update)

    @patch("builtins.input", side_effect=["AGREGAR", "11 Melon 70 13"])
    def test_get_data(self, mock_input):
        response = get_data()
        self.assertEqual(response, ("AGREGAR", [11, "Melon", 70, 13]))

    @patch("builtins.input", side_effect=["AEP", "AyudaEnPython"])
    def test_get_data_error(self, mock_input):
        with self.assertRaises(ValueError) as msg:
            get_data()
        self.assertEqual("", str(msg.exception))

    def test_add(self):
        self.assertTrue(add(self._products, [11, "Melon", 70, 13]))
        self.assertFalse(add(self._products, [11, "Melon", 70, 13]))

    def test_delete(self):
        add(self._products, [11, "Melon", 70, 13])
        self.assertTrue(delete(self._products, [11, "Melon", 70, 13]))
        self.assertFalse(delete(self._products, [14, "Maiz", 45000, 12]))

    def test_update(self):
        self.assertTrue(update(self._products, [1, "Manzanas", 70, 13]))
        self.assertFalse(update(self._products, [14, "Maiz", 45000, 12]))

    def test_statistics(self):
        add(self._products, [11, "Melon", 70, 13])
        self.assertEqual(
            _statistics(self._products),
            ("Jamon", "Melon", "4460.9", "1015010.0")
        )

    def test_output(self):
        add(self._products, [11, "Melon", 70, 13])
        self.assert_stdout(
            "Jamon Melon 4460.9 1015010.0\n",
            function=lambda: output(self._products)
        )

    def test_cases(self):
        for (action, data), expected in zip(self.cases, self.outputs):
            _products = copy.deepcopy(productos)
            with self.subTest(action=action, data=data):
                _actions(action)(_products, data)
                self.assert_stdout(
                    expected,
                    function=lambda: output(_products)
                )


if __name__ == "__main__":
    unittest.main()

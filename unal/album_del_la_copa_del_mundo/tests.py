"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from album import tipolamina, mefaltalamina, notengo, puedocambiar


class TestAlbum(unittest.TestCase):

    def test_tipolamina(self):
        laminas = [
            "escudo",
            "equipo",
            "entrenador",
            "entrenador",
            "equipo",
            "jugador",
            "jugador",
            "jugador",
            "escudo",
        ]
        self.assertEqual(tipolamina(laminas), ["escudo", "equipo", "entrenador", "jugador"])

    def test_mefaltalamina(self):
        faltantes = ([3, 6, 8], [1, 3, 6, 8])
        laminas = (
            [
                "equipo",
                "jugador",
                "escudo",
                "jugador",
                "escudo",
                "escudo",
                "entrenador",
                "equipo",
                "jugador",
            ],
            [
                "entrenador",
                "escudo",
                "jugador",
                "jugador",
                "jugador",
                "equipo",
                "escudo",
                "entrenador",
                "jugador",
                "jugador",
            ],
        )
        tipos = ("jugador", "escudo")
        resultados = ([3, 8], [1, 6])
        for faltante, lamina, tipo, resultado in zip(faltantes, laminas, tipos, resultados):
            self.assertEqual(mefaltalamina(faltante, lamina, tipo), resultado)

    def test_notengo(self):
        a, b = [3, 5, 7, 10, 15, 16], [4, 10, 5, 8]
        self.assertEqual(notengo(a, b), [3, 7, 15, 16])

    def test_puedocambiar(self):
        a, b = [3, 5, 7, 10, 15, 16], [4, 10, 5, 8]
        self.assertEqual(puedocambiar(a, b), 2)


if __name__ == '__main__':
    unittest.main()

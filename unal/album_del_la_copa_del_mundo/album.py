"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

def tipolamina(laminas):
    return sorted(list(set(laminas)), key=laminas.index)


def mefaltalamina(faltantes, laminas, tipo):
    return [posicion for posicion in faltantes if laminas[posicion] == tipo]


def notengo(otras_laminas, mis_laminas):
    return [lamina for lamina in otras_laminas if lamina not in mis_laminas]


def puedocambiar(laminas_a, laminas_b):
    return min(
        len(notengo(laminas_a, laminas_b)),
        len(notengo(laminas_b, laminas_a)),
    )

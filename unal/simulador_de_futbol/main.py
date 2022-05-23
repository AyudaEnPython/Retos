"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Tuple

VALID = ".+T|X-*YW!@#$"
GOL, EMPATE, ATAJADA = "\u00D8", "\u265E", "\u00A5"


def validate(input_: str, valid: str = VALID) -> str:
    if not all(c in valid for c in input_):
        return "!"*len(input_)
    return input_


def es_palindromo(xs: str) -> bool:
    xs = xs.lower(
        ).replace("á", "a"
        ).replace("é", "e"
        ).replace("í", "i"
        ).replace("ó", "o"
        ).replace("ú", "u"
        ).replace(" ", "")
    return xs == xs[::-1]


def sol(xs: str, ys: str) -> Tuple[str, int]:
    s, m = "", 0
    for x in xs:
        c = 0
        for y in ys:
            if ord(x) > ord(y):
                s += GOL
                c += 1
            elif ord(x) < ord(y):
                s += ATAJADA
            else:
                s += EMPATE
        if c > m:
            m = c
    return s, m


def show(o: str, m: int, c: str) -> None:
    print(o)
    print("ES PALINDROMO" if es_palindromo(c) else "NO ES PALINDROMO")
    print(m)


def main():
    a, b, c = input(), input(), input()
    o, m = sol(a, b)
    show(o, m, c)


if __name__ == "__main__":
    main()

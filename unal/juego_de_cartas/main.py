"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Tuple


def _before(s: str, char: str = ",") -> str:
    return s.upper().replace(char, "")


def _after(s: Tuple[str, str], char: str = " ") -> str:
    a, b = s
    return f"{a.replace('', char)}\n{b.replace('', char)}"


def sol(s: str) -> str:
    c = r = ""
    j, k = s[0], 0
    for i in s:
        if i != j:
            r += j
            c += str(k)
            k = 0
        j = i
        k += 1
    r += j
    c += str(k)
    return r, c


def main():
    s = input()
    print(_after(sol(_before(s))))


if __name__ == "__main__":
    main()

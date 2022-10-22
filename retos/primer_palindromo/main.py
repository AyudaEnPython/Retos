"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: needs optimization and tests...
"""
from typing import Tuple, List


def es_palindromo(s: str) -> bool:
    return s == s[::-1]


def f(s: str, l: int, r: int) -> Tuple[int, int]:
    if l < 0 or r > len(s):
        return l+1, r-1
    if s[l] == s[r]:
        return f(s, l-1, r+1)
    else:
        return l, r


def get_words(s: str) -> str:
    t = []
    right = 2
    mid = 1 if len(s) % 2 == 0 else 0
    for i in range(1, len(s)-1):
        l, r = f(s, i-mid, right)
        right += 1
        w = s[l+1:r]
        if len(w) > 1:
            t.append(w)
    return t


def solve(s: str) -> List[str]:
    return [word for word in get_words(s) if es_palindromo(word)]


def main():
    s = "gkaskgjasgjajk12412it21t12tabcbaaskfaskgas219219129c"
    palindromes = solve(s)
    for palindrome in palindromes:
        print(palindrome)


if __name__ == "__main__":
    main()

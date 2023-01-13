"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: needs optimization and tests...
"""
from typing import List


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def all_palindromes(ss: str) -> List[str]:
    r = []
    for i in range(len(ss)):
        for j in range(i, len(ss)):
            s = ss[i:j + 1]
            if is_palindrome(s) and len(s) > 1:
                r.append(s)
    return r


def main():
    INPUT: str = "gkaskgjasgjajk12412it21t12tabcbaaskfaskgas219219129c"
    print(all_palindromes(INPUT))


if __name__ == "__main__":
    main()

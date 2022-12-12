"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

from typing import List


def sol(x: str = "BINGO") -> List[str]:
    return [
        f"{x[i]}{j+1:02d} " for i in range(len(x))
        for j in range(i*15, (15*i)+15)
    ]


print(sol())

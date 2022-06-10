"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Tuple

P, Q = (
    "Mi cacharrito es el mas viejo de todos los autos ;D",
    "Al menos otro auto es mas viejo que mi cacharrito :(",
)


def get_data() -> Tuple[int, List[str]]:
    n = int(input())
    return [input() for _ in range(n)]


def sol(data: List[str], p: str = P, q: str = Q) -> List[str]:
    return "\n".join(
        p if all(map(lambda x: m < x, t)) else q
        for m, *t in map(lambda x: x.split(), data)
    )


def main():
    data = get_data()
    print(sol(data))


if __name__ == "__main__":
    main()

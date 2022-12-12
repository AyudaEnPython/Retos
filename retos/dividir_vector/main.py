"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Tuple

Arr = List[List[int]]


def _get_data() -> Tuple[int, int, Arr]:
    n, k = input().split()
    data = list(map(int, input().split()))
    return int(n), int(k), data


def sol(arr: Arr, n: int, k: int) -> str:
    ts = [arr[i:i+k] for i in range(0, n, k)]
    for t in ts:
        t.append(t.pop(0))
    return " ".join(str(x) for t in ts for x in t)


def main():
    n, k, data = _get_data()
    print(sol(data, n, k))


if __name__ == "__main__":
    main()

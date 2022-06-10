"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List, Tuple


def _table(x: int, y: int) -> int:
    return {
        x < 90 and y < 70: 15,
        90 <= x < 130 and 70 <= y < 90: 0,
        130 <= x < 140 and 90 <= y < 95: 0,
        140 <= x < 150 and 95 <= y < 100: 10,
        150 <= x < 170 and 100 <= y < 110: 10,
        170 <= x < 190 and 110 <= y < 120: 20,
        x >= 190 and y >= 120: 50,
        x >= 150 and y < 100: 20,
    }.get(True, 0)


def get_data() -> Tuple[List[int], List[List[int]]]:
    data = []
    while True:
        try:
            n, m = input().split()
            n, m = int(n), int(m)
            if int(n) < 1:
                continue
            for _ in range(n):
                s = int(input())
                if s < 1:
                    continue
                data.append(s)
            ss = [list(map(int, input().split())) for _ in range(m)]
            if len(data) == n and len(ss) == m:
                break
        except ValueError as e:
            print(e)
    return data, ss


def sol(r: List[int], m: List[List[int]]) -> Tuple[List[int], Dict[int, int]]:
    t = [i for i in r]
    _d = {k:0 for k in range(len(t))}
    for i, s, d in m:
        n = _table(s, d)
        t[i-1] -= n
        if i not in _d:
            _d[i] = n
        else:
            _d[i] += n
    return t, _d


def _percentage(x: int, y: int) -> float:
    return round(y * 100 / x, 2)


def min_max(arr: List[int]) -> str:
    min_, max_ = min(arr), max(arr)
    i_min, i_max = arr.index(min_), arr.index(max_)
    return (i_min, min_), (i_max, max_)


def output(r: List[int], t: List[int], m: Dict[int, int]) -> None:
    print("\n".join(f"{i+1} {v}" for i, v in min_max(t)))
    for i in range(1, len(t)+1):
        print(f"{i} {_percentage(r[i-1], m[i]):.2f}%")


def main():
    r, s = get_data()
    t, m = sol(r, s)
    output(r, t, m)


if __name__ == "__main__":
    main()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Any, Dict, List

FILENAME = "data.csv"
BRANCHES = 32
N = 5


def _table(x: int, y: int) -> bool:
    return {
        x < 91 and y < 63: True,
        91 <= x < 134 and 63 <= y < 77: False,
        134 <= x < 162 and 77 <= y < 105: False,
        162 <= x < 188 and 105 <= y < 119: True,
        188 <= x < 201 and 119 <= y < 126: True,
        201 <= x < 214 and 126 <= y < 146: True,
        x >= 214 and y >= 146: True,
        x >= 152 and y < 77: True,
    }.get(True, 0)


def get_data(n: int = 2) -> List[List[Any]]:
    data = []
    with open(FILENAME, "r") as f:
        next(f)
        for line in f.read().splitlines():
            tmp = line.split(",")
            data.append(tmp[n:N]+list(map(int, tmp[N:])))
    return data


def _mean(data: Dict[int, Dict[str, Any]]) -> Dict[int, float]:
    for i in range(1, BRANCHES+1):
        data[i]["mean"] = round(sum(data[i]["mean"])/len(data[i]["mean"]), 2)
    return data


def sol(data: List[List[Any]]) -> Dict[int, Dict[str, Any]]:
    _d = {
        k: {
            "header": "",
            "male": 0,
            "female": 0,
            "mean": [],
            "total": 0,
        }
        for k in range(1, BRANCHES+1)
    }
    for g, c, d, i, _, mq, sp, dp in data:
        _d[i]["header"] = f"{i} {c} {d}"
        if _table(sp, dp):
            _d[i]["mean"] += [mq] 
            _d[i]["total"] += mq
            if g == "m":
                _d[i]["male"] += 1
            else:
                _d[i]["female"] += 1
    return _mean(_d)


def output(data: Dict[int, Dict[str, Any]], n: int) -> None:
    d = data[n]
    print(f"{d['header']}")
    print("scheduled patients")
    print(f"male {d['male']}")
    print(f"male {d['female']}")
    print(f"total {d['male'] + d['female']}")
    print("scheduled medicine quantity")
    print(f"mean {d['mean']}")
    print(f"total {d['total']}")


def main():
    data = sol(get_data())
    n = input()
    output(data, int(n))


if __name__ == "__main__":
    main()

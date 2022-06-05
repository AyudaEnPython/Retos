"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import json
from typing import Dict, Tuple


def get_data() -> Tuple[Dict[str, int], str]:
    return json.loads(input()), input()


def sol_1(d: Dict[str, float], s: str) -> Tuple[str, str]:
    r, t = "", 0
    for k, v in d.items():
        if k in s:
            r += k + " "
            t += v
    return r[:-1], str(t)


def sol_2(d: Dict[str, float], s: str) -> Tuple[str, str]:
    found = [c for c in s.split(" ") if c in d]
    return " ".join(found), str(sum(d[c] for c in found))


def main(): 
    data, s = get_data()
    print("\n".join(sol_1(data, s)))
    # print("\n".join(sol_2(data, s)))


if __name__ == "__main__":
    main()

"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import json
from typing import Dict, Tuple


def get_data() -> Tuple[Dict[str, int], str]:
    return json.loads(input()), input()


def sol(d: Dict[str, float], s: str) -> Tuple[str, str]:
    r, t = "", 0
    for k, v in d.items():
        if k in s:
            r += k + " "
            t += float(v)
    return r, str(t)


def main(): 
    data, s = get_data()
    print("\n".join(sol(data, s)))


if __name__ == "__main__":
    main()

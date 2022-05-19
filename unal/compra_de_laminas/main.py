"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import json
from typing import Dict, Tuple


def get_data() -> Tuple[Dict[str, int], str]:
    return json.loads(input()), input()


def sol(d: Dict[str, int], s: str) -> Tuple[int, str]:
    return (
        str(sum([d[k] for k in d if k in s])),
        " ".join(c for c in s if c in d)
    )


def main(): 
    data, s = get_data()
    print("\n".join(sol(data, s)))


if __name__ == "__main__":
    main()

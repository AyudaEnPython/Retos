"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from data import followers
from typing import Dict, List


def get_friends(data: Dict[int, List[int]]) -> Dict[int, List[int]]:
    return {k: [v for v in data[k] if k in data[v]] for k in data}


def main():
    print(get_friends(followers))


if __name__ == "__main__":
    main()

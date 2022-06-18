"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
from datetime import timedelta


def get_data() -> List[str]:
    n = int(input())
    return [input() for _ in range(n)]


def _to_str(time_d: timedelta) -> str:
    h, r = divmod(time_d.seconds, 3600)
    m, s = divmod(r, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def sol(time: str) -> str:
    m, s = time.split(":")
    a = timedelta(hours=int(m), minutes=(int(s)))
    b = timedelta(minutes=int(m), seconds=int(s))
    return _to_str(a - b)


def main():
    for time in get_data():
        print(sol(time))


if __name__ == "__main__":
    main()

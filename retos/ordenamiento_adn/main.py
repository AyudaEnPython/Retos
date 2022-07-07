"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from cgi import print_arguments
from typing import List, Tuple

ALLOWED = "ACGT"
MIN_N, MIN_ADN, MAX = 1, 5, 50
FILENAME = "ADN.dat"


def _validate_dna(dna: str) -> str:
    if not dna:
        raise ValueError("Error: el ADN no puede ser vacio")
    for nucleotide in dna:
        if nucleotide not in ALLOWED:
            raise ValueError(
                f"Error: el ADN contiene un nucleotido no permitido: "
                f"{nucleotide}"
            )
    return dna


def _validate_n(n: str, min: int, max: int) -> int:
    if not n:
        raise ValueError("Error: 'n' no puede ser vacio")
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Error: 'n' debe ser un numero entero")
    if n < min or n > max:
        raise ValueError("Error: 'n' debe ser mayor a 0")
    return n


def get_data(filename: str) -> Tuple[Tuple[str, ...], List[str]]:
    data = []
    with open(filename, "r") as f:
        values = tuple(next(f).strip() for _ in range(3))
        tmp = []
        for line in f.read().splitlines():
            if line:
                tmp.append(line)
            else:
                data.append(tmp)
                tmp = []
        data.append(tmp)
    return values, data


def clean_up(data: List[List[str]], values: int) -> Tuple[int, List[str]]:
    try:
        cases, xy, q = values
        x, y = xy.split(" ")
        cases = _validate_n(cases, MIN_N, MAX)
        if cases != len(data):
            raise ValueError(
                f"Error: el numero de casos es incorrecto: "
                f"{cases} != {len(data)}"
            )
        x = _validate_n(x, MIN_ADN, MAX)
        y = _validate_n(y, MIN_ADN, MAX)
        q = _validate_n(q, MIN_N, MAX)
        for case in range(cases):
            data[case] = [_validate_dna(dna) for dna in data[case]]
    except ValueError as e:
        print(e)
        return 0, []
    return cases, data


def sol(arr: List[str]) -> List[Tuple[str, int]]:
    n, k = len(arr), 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                k += 1
                # arr[i], arr[j] = arr[j], arr[i] : just in case for variants
    return "".join(arr), k


def sorted_(data: List[str]) -> List[Tuple[str, int]]:
    return sorted([sol(list(dna)) for dna in data], key=lambda x: x[1])


def show(data: List[str]):
    for dna, _ in data:
        print(dna)


def main():
    values, data = get_data(FILENAME)
    n, data = clean_up(data, values)
    for i in range(n):
        d_ = sorted_(data[i])
        show(d_)


if __name__ == "__main__":
    main()

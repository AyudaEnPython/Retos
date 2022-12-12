#!/usr/bin/python3
"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

*    Estatus    : AC 
*    Porcentaje : 100.00%
*    Memoria    : 10.81 MB
*    Tiempo     : 0.39s

"""
from sys import stdin, stdout


def _get_data():
    _ = stdin.readline()
    return [int(x) for x in stdin.readline().split()]


def sol(data):
    T = {32: "XS", 36: "S", 38: "M", 40: "L", 42: "XL"}
    return {T[k]: data.count(k) for k in T}


def _output(data):
    for k, v in data.items():
        stdout.write("{}:{}:{}\n".format(k, v, v*12))


def _main() -> None:
    data = _get_data()
    _output(sol(data))


if __name__ == "__main__":
    _main()

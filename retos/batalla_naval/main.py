"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
# pip install prototools
from prototools import matrix, show_matrix, int_input

WIDTH, HEIGHT = 9, 9
SEA, SHIP = "~", "#"
MISSED, HIT = "O", "X"
Board = List[List[str]]


def read_input(n: int):
    return [int_input(min=0, max=WIDTH-1) for _ in range(n)]


def place_ship(board: Board, x: int, y: int, size: int, orient: int) -> None:
    if orient:
        for i in range(size):
            board[x][y + i] = SHIP
    else:
        for i in range(size):
            board[x + i][y] = SHIP


def attack(board: Board, x: int, y: int) -> None:
    if board[x][y] == SHIP:
        board[x][y] = HIT
    elif board[x][y] == SEA:
        board[x][y] = MISSED


def main():
    board: Board = matrix(WIDTH, HEIGHT, precision=1, char=SEA)
    for _ in range(2):
        place_ship(board, *read_input(4))
        print()
    show_matrix(board, borderless=True, width=1)
    attack(board, *read_input(2))
    print()
    show_matrix(board, borderless=True, width=1)


if __name__ == "__main__":
    main()

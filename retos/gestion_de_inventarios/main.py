"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Any, Callable, Dict, List, Tuple

ACTIONS = "AGREGAR", "BORRAR", "ACTUALIZAR"
Data = List[Any]
productos: Dict[int, Data] =  {
    1: ['Manzanas', 5000.0, 25],
    2: ['Limones', 2300.0, 15],
    3: ['Peras', 2700.0, 33],
    4: ['Arandanos', 9300.0, 5],
    5: ['Tomates', 2100.0, 42],
    6: ['Fresas', 4100.0, 3],
    7: ['Helado', 4500.0, 41],
    8: ['Galletas', 500.0, 8],
    9: ['Chocolates', 3500.0, 80],
    10: ['Jamon', 15000.0, 10],
}


def _actions(command: str) -> Callable:
    return {
        "AGREGAR": add, "BORRAR": delete, "ACTUALIZAR": update
    }[command]


def get_data() -> Tuple[str, Data]:
    command = input()
    if command not in ACTIONS:
        raise ValueError
    try:
        data = input().split(" ")
    except ValueError:
        raise ValueError
    id_, name, price, quantity = data
    return command, [int(id_), name, float(price), int(quantity)]


def delete(products: Dict[int, Data], data: Data) -> bool:
    id_, *_ = data
    if id_ in products:
        del products[id_]
        return True
    return False


def update(products: Dict[int, Data], data: Data) -> bool:
    id_, *values = data
    if id_ in products:
        products[id_] = values
        return True
    return False


def add(products: Dict[int, Data], data: Data) -> bool:
    id_, *values = data
    if id_ not in products:
        products[id_] = values
        return True
    return False


def _statistics(products: Dict[int, Data]) -> Tuple[str, ...]:
    max_ = max(products.values(), key=lambda x: x[1])[0]
    min_ = min(products.values(), key=lambda x: x[1])[0]
    mean_ = sum(x[1] for x in products.values()) / len(products)
    value = sum(x[1]*x[2] for x in products.values())
    return max_, min_, f"{mean_:.1f}", f"{value:.1f}"


def output(products: Dict[int, Data]) -> None:
    print(" ".join(x for x in _statistics(products)))


def main():
    try:
        action, data = get_data()
    except ValueError:
        print("ERROR")
        return
    else:
        if _actions(action)(productos, data):
            output(productos)
        else:
            print("ERROR")


if __name__ == "__main__":
    main()

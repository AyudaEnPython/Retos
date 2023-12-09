from typing import Callable

line = "Alice ventured to taste it, and finding it very nice,(it had, in fact," \
    "a sort of mixed flavour of cherry-tart, custard, pine-apple, roast turkey, "\
    "toffee, and hot buttered toast,) she very soon finished it off. "\
    "She had never forgotten that if you drink much from a bottle marked “poison,” "\
    "it is almost certain to disagree with you, sooner or later."\


def _f(w: str, ow: str, g: Callable[[str, str], bool]) -> bool:
    return len(w) > len(ow) and all(g(w[i], w[i+1]) for i in range(len(w)-1))


def main():
    ws = ["".join([c for c in ws if c.isalpha()]) for ws in line.split()]
    la = lr = ""
    for w in ws:
        if _f(w, la, lambda x, y: x <= y):
            la = w
        if _f(w, lr, lambda x, y: x >= y):
            lr = w
    print(f"Longest in alphabetical order: {la}")
    print(f"Longest in reverse alphabetical order: {lr}")


if __name__ == "__main__":
    main()

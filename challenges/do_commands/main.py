import re
from turtle import Screen, Turtle, done


def _parse(ss):
    return tuple(zip(
        tuple(s for s in ss if not s.isdigit()),
        tuple(map(int, re.findall('-?\d+\.?\d*', ss))),
    ))


def _action(t, s, x=None):
    return {
        "R": lambda: t.rt(x), "L": lambda: t.lt(x),
        "F": lambda: t.fd(x), "P": lambda: t.width(x),
        "U": t.pu, "D": t.pd, "B": t.begin_fill, "E": t.end_fill,
    }[s]()


def do_commands(t, ss):
    m = _parse(ss)
    if m[0][0] == "*":
        for _ in range(m[0][1]):
            for a, x in m[1:]:
                _action(t, a, x)
    else:
        for a, x in m:
            _action(t, a, x)


def setup_cur(t, color, *pos):
    t.color(color)
    t.penup()
    t.setpos(pos)
    t.ht()


def main():
    s, g, b = Screen(), Turtle(), Turtle()
    s.bgcolor("red")
    s.setup(410, 420)
    setup_cur(g, "green", -95, -50)
    setup_cur(b, "brown", -90, -100)
    g.speed(0)
    do_commands(g, "D0B0")
    do_commands(g, "*12L60F15R120F15L60")
    do_commands(g, "L120")
    do_commands(g, "*12L60F15R120F15L60")
    do_commands(g, "L120")
    do_commands(g, "*12L60F15R120F15L60")
    do_commands(g, "E0L120U0F90R90D0P10F90")
    do_commands(b, "F25D0B0R85F100L85F100L85F100R85E0")
    done()


if __name__ == "__main__":
    main()

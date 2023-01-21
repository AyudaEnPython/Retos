from turtle import Screen, Turtle, done

SPACE = 20
DATA = [
    "John Smith",
    "Graham Jones",
    "Beaumont",
    "George William Booker",
    "Ivy Smithers",
    "Fox",
    "Lee",
    "Mary Constance Green",
]


def _max(ss, k):
    return max(ss, key=lambda x: x[k])[k]


def _T(data, x=SPACE):
    return {i: (x - 2) * i + x for i in range(_max(data, "h") + 1)}


def _box(t, w, h):
    t.pd()
    for x in (w//2, h, w, h, w//2):
        t.lt(90)
        t.fd(x)
    t.rt(90)
    t.pu()


def transform(data):
    return [{
        "s": "\n".join(s.split()),
        "w": len(max(s.split(), key=len)),
        "h": s.count(" "),
    } for s in data]


def display(t, data, line=True, style="Courier", size=12, space=SPACE):
    T, len_ = _T(data), len(data)
    for i, d in enumerate(data, 1):
        w, h = d["w"], T[d["h"]]
        t.fd(h + space)
        t.write(d["s"], align="center", font=(style, size))
        w *= size
        _box(t, w, h)
        if i != len_:
            if line:
                t.pd()
            t.fd(space)
            t.pu()
            t.bk(space)


def get_wh(data, space=SPACE):
    return (
        _max(data, "w") * space + 4,
        (sum(value["h"] + 1 for value in data) + len(data) + 1) * space,
    )


def setup(w, h, speed=0):
    s, t = Screen(), Turtle()
    s.setup(w, h)
    t.ht()
    t.speed(speed)
    t.pu()
    t.rt(90)
    t.setpos(0, h // 2)
    return t


def main():
    data = transform(DATA)
    t = setup(*get_wh(data))
    display(t, data)
    done()


if __name__ == "__main__":
    main()

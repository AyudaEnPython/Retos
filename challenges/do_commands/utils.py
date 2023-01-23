import re
from itertools import groupby


def _parse(ss):  # using re
    return tuple(zip(
        tuple(s for s in ss if not s.isdigit()),
        tuple(map(int, re.findall('-?\d+\.?\d*', ss))),
    ))


def _parse_iter(ss):  # using itertools
    return tuple(zip(*[iter(
        int(x) if x.isdigit() else x
        for x in ("".join(g) for _, g in groupby(ss, str.isdigit))
    )]*2))


def _parse__(ss):  # no libraries
    a = tuple(s for s in ss if not s.isdigit())
    b, n = [], ""
    for s in ss:
        if s not in a:
            n += s
        else:
            if n:
                b.append(int(n))
            n = ""
    b.append(int(n))
    return tuple(zip(a, b))

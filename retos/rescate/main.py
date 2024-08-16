"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import time
import matplotlib.pyplot as plt


def get_data(filename="input.txt"):
    with open(filename) as f:
        data = f.read().splitlines()
    return [list(map(int, line.split())) for line in data]


def write_data(data, filename="output.txt"):
    with open(filename, "w") as f:
        f.write("\n".join(data))


def f(x, y, z):
    t = i = 0
    while True:
        t += x
        i += 3
        if t >= z:
            break
        if t < 0:
            return -1
        t -= y
        i += 1
    return i


def g(f, a, b, c):
    start = time.perf_counter()
    f(a, b, c)
    end = time.perf_counter()
    return 0, end - start


def h(t):
    return t[1] - t[0]


def plot_(times):
    d = {k: v for k, v in zip(range(1, len(times)+1), times)}
    for k, v in d.items():
        plt.plot(v, label=k)
    plt.ylabel("Time(s)")
    plt.legend()
    plt.show()


def main():
    data = get_data()
    output = [
        f"{a} {b} {c} {f(a, b, c)} {h(g(f, a, b, c)):.5f}"
        for (a, b, c) in data
    ]
    times = sorted(g(f, *line) for line in data)[::-1]
    plot_(times)
    write_data(output)


if __name__ == "__main__":
    main()

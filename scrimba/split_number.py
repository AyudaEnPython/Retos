"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - SPLIT NUMBER **

Write code to split/print numbers into digits as below

nums = [321, 410, 987, 1297]

output: '[[3, 2, 1], [4, 1, 0], [9, 8, 7], [1, 2, 9, 7]]'

Bonus: add first numbers in each sub-list (3+4+9+1)

output: '[17, 13, 17, 7]'
"""

xs = [321, 410, 987, 1297]
xs = [[int(y) for y in str(x)] for x in xs]
print(xs)

# ---------------------------------------------------------------- bonus

xs = [321, 410, 987, 1297]
ys = [str(y) for y in xs]
ys = [x + '0'*(max(len(str(x)) for x in xs) - len(x)) for x in ys]
ys = [sum(map(int, i)) for i in zip(*ys)]
print(ys)

# -------------------------------------------------------- bonus alt ver
xs = [321, 410, 987, 1297]
xs = [str(x) for x in xs]
z = []
for i in range(len(xs[::-1])):
    t_ = []
    for j in range(max([len(x) for x in xs])):
        try:
            t_.append(int(xs[j][i]))
        except IndexError:
            continue
    z.append(sum(t_))
print(z)

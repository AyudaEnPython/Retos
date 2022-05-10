"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - PLOT AREAS **

A tropical paradise realtor has landplots below for sale
['ID', lenght, width] in multiples of 10 m (5 = 50m)
Write code to help them sort list by plot area

plots = [['A', 3, 3], ['B', 5, 2], ['C', 6, 6], ['D', 4, 8], ['E', 11, 2]]

# output
'Plots in descending order:
C(6,6), D(4,8), E(11,2), B(5,2), A(3,3)'
"""

plots = [['A', 3, 3], ['B', 5, 2], ['C', 6, 6], ['D', 4, 8], ['E', 11, 2]]


def sol(arr):
    return ", ".join(
        f"{s}({x},{y})" for s, x, y in
        sorted(arr, key=lambda x: x[1]*x[2], reverse=True)
    )


if __name__ == "__main__":
    print("Plots in descending order:")
    print(sol(plots))

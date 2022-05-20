"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - SORT SHOES **

You have a list of all shoes in your small sotre [model, size].
Sort and print list of all  shoes by model and size.

shoes = [
    ['B', 9], ['A', 8], ['A', 7], ['C', 9],
    ['A', 9], ['B', 7], ['C', 8], ['B', 8],
]

# output (by model, then size)
Sorted shoes:
A - 7
A - 8
A - 9
B - 7
B - 8
B - 9
C - 8
C - 9

# bonus 1. Can you also sort by first siez, and then model?
"""

shoes = [
    ['B', 9], ['A', 8], ['A', 7], ['C', 9],
    ['A', 9], ['B', 7], ['C', 8], ['B', 8],
]

print("Sorted shoes:")
print(
    "\n".join(
        f"{i[0]} - {i[1]}" for i
        in sorted(shoes, key=lambda x: (x[0], x[1]))
    )
)

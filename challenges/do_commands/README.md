# Do Commands

Can you write the `do_commands()` function required to complete this
turtle graphics script?

What picture do you get when the script is completed and run?

```python
import turtle

turtle.bgcolor("red")
t1 = turtle.Turtle()
t1.speed(0)
t1.color("green")
t1.penup()
t1.setposition(-95, -50)
t1.pendown()
t1.begin_fill()
do_commands(t1, "*12L60F15R120F15L60")
t1.left(120)
do_commands(t1, "*12L60F15R120F15L60")
t1.right(-120)
do_commands(t1, "*12L60F15R120F15L60")
do_commands(t1, "E0L120U0F90R90D0P10F90")
t2 = turtle.Turtle()
t2.penup()
t2.setposition(-90, -100)
t2.color("brown")
do_commands(t2, "F25D0B0R85F100L85F100L85F100R85E0")
turtle.screensize(900, 700)
turtle.done()
```

`do_commands()` takes 2 parameters, the turtle to use (`t`), and a string
of abbreviated commands, e.g. `L15` becomes `t.left(15)`
Other command abbreviations. These 3 all take one numeric parameter

    R => right()
    F => forward()
    P => pensize()

The following commands are followed by a `0` (zero). They resolve to
turtle commands that take no parameter

    U0 -> up()
    D0 -> down()
    B0 -> begin_fill()
    E0 -> end_fill()

When the command string starts with `*` and a number, the rest of the
command string is to be repeated number times.

---
Author: Mike Kerry

Link: https://www.facebook.com/groups/python/permalink/1339507880223106/
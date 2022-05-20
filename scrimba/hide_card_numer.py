"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - HIDE CARD NUMBER **

Write code to take in a 16 digit integer card number and output 'hidden
card' displaying only the last 4 digits.

input = 4154455441155555

output = 'Your card: **** **** **** 5555'

# Bonus - output hidden number but also openly display any 1's that
occur in the card number

output = 'Your card: *1** **** *11* 5555'
"""


def hide_card_number(card_number, char="*", show_digit=None):
    if show_digit is None:
        hidden = "".join(char for _ in card_number[:-4])
    else:
        hidden = "".join(
            char if i != str(show_digit) else i for i in card_number[:-4]
        )
    return hidden + card_number[-4:]


def format_card(hidden_number, sep=" ", size=4):
    return sep.join(
        hidden_number[i:i+size] for i in range(0, len(hidden_number), size)
    )


def show(hidden_number):
    print(f"Your card: {format_card(hidden_number)}")


show(hide_card_number("4154455441155555"))
show(hide_card_number("4154455441155555", show_digit=1))

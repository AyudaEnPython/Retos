"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - BIEBER STRUGGLES IN SINGAPORE **

Justin is in singapore for holiday. while at a cafe, he is mistaken for
do kwon, founder of Luna(crypto) and snatched by a russian hit squad.
Russian opsec being what it is, police intercept unecrypted, but coded
message from a phone immediately after. They want 1,000 btc to release
Justin. Police are clueless, and ask you for help in decoding message.

You know FSB used code, where each letter gets a value, which is
doubled, 'a','b' are 5 and 6 and so on. Then every other 2-digit
number/character starting at second position is reversed so that
'abcdef' encodes to=>'102014161812' (afcdeb)
write code to decode and output the message and help save Justin!

intercept = '1242263422322626121816404638362648184618341226364644'

EDIT: clearer example:
message 'abcdef' to encode it to 'secret string' you do the following

First you give every char a number and double it a starts at 5 so
10, 12,14,16,18,20

then you take chars in position 1,3,5 (12,16,20) and reverse their
order (20,16,12) and put them back into string in 'same position'
So you get
10,20,14,16,18,12
"""

intercept = "1242263422322626121816404638362648184618341226364644"
decoder = {
    str(v*2):k for k, v in zip(
        "abcdefghijklmnopqrstuvwxyz", range(5, 32)
    )
}


def decoded(s):
    ss = [s[i:i+2] for i in range(0, len(s), 2)]
    odd, even = ss[1::2][::-1], ss[::2]
    return [even[i//2] if i % 2 == 0 else odd[i//2] for i in range(len(ss))]


def show(ss):
    print("".join(decoder[s] for s in ss))


show(decoded(intercept))

# Longest word in alphabetic sequence

A Python exercise. From the text given below (an extract from _"Alice in Wonderland"_), find the longest word in which the letters occur in alphabetic sequence. Also find the longest word where the letters occur in reversed alphabetic sequence.
For example, in the word `"got"` the letters occur in alphabetic sequence (in the alphabet, `o` comes after `g` and `t` comes after `o`). In the word `"weed"` the letters occur in reversed alphabetic sequence.

For this task, a `"word"` is any sequence of all alphabetic characters.

> _ADDITION_: Can you solve it with a time complexity of $O(n)$? i.e. with just one loop though the text, and no sorting.

Here is the text:

```python
line = "Alice ventured to taste it, and finding it very nice,(it had, in fact, " \
         "a sort of mixed flavour of cherry-tart, custard, pine-apple, roast turkey, " \
         "toffee, and hot buttered toast,) she very soon finished it off. " \
         "She had never forgotten that if you drink much from a bottle marked “poison,” " \
         "it is almost certain to disagree with you, sooner or later."
```

---

Author: Mike Kerry

Link: https://www.facebook.com/groups/python/permalink/1543637869810105/

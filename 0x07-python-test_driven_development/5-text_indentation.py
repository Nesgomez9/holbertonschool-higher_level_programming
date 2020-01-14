#!/usr/bin/python3

"""Function that makes indentation to a text"""


def text_indentation(text):

    """Function that makes indentation to a text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) == 0:
        print(end='')
        return None
    new_list = list(text)
    for i in [".", "?", ":"]:
        text = text.replace(i, i + "\n\n")
    x = text.split("\n")
    for i in range(len(x) - 1):
        x[i] = x[i].strip()
        print(x[i])
    x[i + 1] = x[i + 1].strip()
    print(x[i + 1], end='')

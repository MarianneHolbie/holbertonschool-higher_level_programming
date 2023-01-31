#!/usr/bin/python3
"""
    Module that contain only one function to indentation text

"""


def text_indentation(text):
    """
    Fonction that print a text with 2 new lines
    after each of these characters: ., ? and :

    Args :
        text: string

    Return:
        indented tring

    Raises:
        Test TypeError

    """
    list_char = [".", "?", ":"]
    i = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    while (i < len(text)):

        if text[i] in list_char:
            print("\n")
            while text[i + 1] == " " and i + 1 < len(text):
                i += 1
        else:
            print("{}".format(text[i]), end="")
        i += 1

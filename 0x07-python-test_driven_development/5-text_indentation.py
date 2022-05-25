#!/usr/bin/python3
"""
The function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function: text_indentation
        prints a text with 2 new lines
    after each of these characters: ., ? and :
    @text: string
    Return: None
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        print(text.replace(". ", ".\n\n").replace(": ", ":\n\n")
              .replace("? ", "?\n\n").lstrip())

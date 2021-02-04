#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie Assignment: rot13
"""

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Benjamin Feder"

import sys
from string import ascii_lowercase, ascii_uppercase


def rotate(message):
    """
    Returns the encoded or decoded message.
    """
    rot_message = ''
    for letter in range(len(message)):

        change = 13

        value = ord(message[letter])

        if value + change > 122:
            change -= (122 - value)
            change = change % 26
            rot_message += chr(96 + change)

        else:
            rot_message += chr(value + change)

    return rot_message


def main(args):
    """Main program code."""
    if len(args) != 1:
        print('usage: python rot13.py message')
        sys.exit(1)

    message = sys.argv[1]

    rot = rotate(message)
    print(rot)


if __name__ == '__main__':
    main(sys.argv[1:])

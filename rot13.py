#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie Assignment: rot13
"""

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Benjamin Feder, http://www.asciitable.com/, geeksforgeeks.org"

import sys
from string import ascii_lowercase, ascii_uppercase


def rotate(message):
    """
    Returns the encoded or decoded message.
    """
    rot_message = ''
    for letter in range(len(message)):

        change = 13

        # ord() returns the number representing a specific character's unicode
        value = ord(message[letter])

        if value < 65 or (value > 90 and value < 97) or value > 122:
            rot_message += chr(value)

        elif value + change > 122:  # 122 is the last lowercase 'z' in ASCII
            change -= (122 - value)
            change = change % 26  # 26 letters in the alphabet

            # 96 is the last character before 'a' in ASCII
            # chr() returns the character that represents the specified unicode number
            rot_message += chr(96 + change)

        elif value > 64 and value < 91:
            if value + change > 90:
                rot_message += chr(value - change)
            else:
                rot_message += chr(value + change)

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

"""Codewars kata https://www.codewars.com/kata/get-the-middle-character/train/python."""

def get_middle(s):
    """Return the middle letter of an odd string or the the two middle letters of an even string."""
    if len(s) % 2 == 0:
        return s[int(len(s)/2 - 1) : int(len(s)/2 + 1)]
    return s[int(len(s)/2)]

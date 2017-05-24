"""The multiples of numbers (8th kata)."""


""" Best practice:
def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
"""


def find_multiples(integer, limit):
    """Function that returns multiples of numbers between given parameters."""
    return list(range(integer, limit + 1, integer))

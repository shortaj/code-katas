"""Find the odd int (6th kata)."""

"""Best Practices:
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


def find_it(seq):
    """Return the first odd repeat of numbers in list."""
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

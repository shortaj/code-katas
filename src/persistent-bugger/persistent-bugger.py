"""The Persistent bugger (6th kata)."""

"""Best Practice:
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
"""


def persistence(n):
    """Multiply each single integer in n until there is one integer."""
    counter = 0
    while len([int(d) for d in str(n)]) != 1:
        n = reduce(lambda x, y: x * y, [int(d) for d in str(n)])
        counter += 1
    return counter

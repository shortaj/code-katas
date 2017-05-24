"""The Highest and Lowest (7th kata)."""


"""Best Practice:
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
"""


def high_and_low(numbers):
    """Take list of string integers and returns highest and lowest."""
    results = sorted([int(n) for n in numbers.split(' ')])
    return ' '.join([str(results[len(results) - 1]), str(results[0])])

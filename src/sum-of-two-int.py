"""The sum of the two lowest positive integers (6th kata)."""

"""Best Practice:
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""


def sum_two_smallest_numbers(numbers):
    """Doesn't change given parameter while summing two lowest pos. int."""
    sum_list = []
    for i in numbers:
        if i > 0:
            sum_list.append(i)
    sum_list.sort()
    return sum_list[0] + sum_list[1]

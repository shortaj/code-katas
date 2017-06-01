"""Checks for proper parenthesis."""


def parenthesis_checker(text):
    """Parse given text for proper use of parenthesis."""
    txt_list = list(text)
    counter = 0
    test_list = []
    for char in txt_list:
        if counter == -1:
            return -1
        elif char == '(':
            test_list.extend(char)
            counter += 1
        elif char == ')':
            test_list.extend(char)
            counter -= 1
    if counter == 0:
        return 0
    elif counter > 0:
        return 1
    else:
        return -1

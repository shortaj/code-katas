"""The python file that holds all functions relating to the codewars kata String-Pyramid."""


def watch_pyramid_from_the_side(characters):
    """Generate a display of the given characters in a pyramid from the side."""
    concat = ''
    if characters:
        for i in range(len(characters)):
            concat = ('\n' + (' ' * i) + (characters[i] * ((len(characters) * 2) - 1 - (i * 2))) + (' ' * i)) + concat
        return concat[1:]
    return characters


def watch_pyramid_from_above(characters):
    """Generate a display of the given characters in a pyramid from above."""
    concat = []
    if characters:
        for i in range(len(characters)):
            concat.append('\n' + characters[:i] + (characters[i] * ((len(characters) * 2) - 1 - (i * 2))) + characters[:i][::-1])
        concat.extend(concat[:len(characters) - 1][::-1])
        return ''.join(concat)[1:]
    return characters


def count_visible_characters_of_the_pyramid(characters):
    """Return the number of showing blocks in a given pyramid."""
    if characters:
        return (len(characters) + (len(characters) - 1)) ** 2
    return -1


def count_all_characters_of_the_pyramid(characters):
    """Return the number of blocks in a given pyramid."""
    if characters:
        return sum(list(map(lambda x: ((x + (x - 1)) ** 2), range(1, len(characters) + 1))))
    return -1

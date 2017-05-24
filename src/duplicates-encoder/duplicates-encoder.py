"""The duplicates encoder(6th kata)."""


"""Best Practices:
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])"""


def duplicate_encode(word):
    """Return a string of (,) based on whether there are duplicate char."""
    return_string = []
    list_holder = word.lower()
    for i in range(len(list_holder)):
        if list_holder.count(list_holder[i]) > 1:
            return_string.insert(i, ')')
        else:
            return_string.insert(i, '(')
    return ''.join(return_string)

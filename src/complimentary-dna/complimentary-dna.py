"""The complimentary dna (7th kata)."""

"""Best Practice:
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

"""


def DNA_strand(dna):
    """Return a complimentary dna strand."""
    return_list = []
    list_dna = list(dna)
    for char in list_dna:
        if char == "A":
            return_list.append('T')
        elif char == "T":
            return_list.append('A')
        elif char == "G":
            return_list.append('C')
        else:
            return_list.append('G')
    return ''.join(return_list)

"""Sorts any given cards into a proper value."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank."""
    return sorted(cards, key='A23456789TJQK'.index)

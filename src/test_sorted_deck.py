"""."""
from sorted_deck import sort_cards


def test_sorted_deck():
    """Test the output of the sorted deck function."""
    assert sort_cards(list('TAKJQ89674523')) == ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    assert sort_cards(list('A98765432TKJQ')) == ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    assert sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']) == ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

"""The test file for proper-parenthetics."""
import pytest

TEST_DICT = [
    ('sdnfasjldnfjkod', 0),
    (')(', -1),
    ('()', 0),
    ('()()()()()(((((', 1),
    ('asdfn((((asd nfkln)))())', 0),
    ('NJCNE3e9(kmsdc))(', -1)
]


@pytest.mark.parametrize('text, int_output', TEST_DICT)
def test_parenthesis_checker(text, int_output):
    """Give several strings of text with multiple desired returns."""
    from proper_parenthetics import parenthesis_checker
    assert parenthesis_checker(text) == int_output

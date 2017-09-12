"""Test for get_middle."""

def test_get_middle():
    from get_middle import get_middle
    assert get_middle('asdfg') == 'd'
    assert get_middle('as') == 'as'
    assert get_middle('a') == 'a'
    assert get_middle('') == ''
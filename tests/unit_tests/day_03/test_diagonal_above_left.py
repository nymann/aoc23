from aoc23.day_03.finding_strategies.adjacent_diagonal_above_left_finder import AdjacentDiagonalAboveLeftFinder


def test_no_line_above():
    finder = AdjacentDiagonalAboveLeftFinder("1..###", 3)
    actual = finder.find(0, 1)
    expected = False
    assert actual == expected


def test_line_above_no_symbol():
    finder = AdjacentDiagonalAboveLeftFinder("...#1#", 3)
    actual = finder.find(index=4, number_length=1)
    expected = False
    assert actual == expected


def test_has_symbol():
    finder = AdjacentDiagonalAboveLeftFinder("#..#1#", 3)
    actual = finder.find(index=4, number_length=1)
    expected = True
    assert actual == expected


def test_above_has_no_symbol_but_line_contains_symbols():
    finder = AdjacentDiagonalAboveLeftFinder(".###1#", 3)
    actual = finder.find(index=4, number_length=1)
    expected = False
    assert actual == expected

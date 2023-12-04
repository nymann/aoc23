from aoc23.day_03.adjacent_symbol_finder import has_adjacent_symbol
from aoc23.day_03.finding_strategies.adjacent_before_finder import AdjacentBeforeFinder


def test_has_adjacent_symbol_to_the_left():
    puzzle_input = "^12"
    index = 1
    line_length = len(puzzle_input)

    finder = AdjacentBeforeFinder(
        puzzle_input=puzzle_input,
        line_length=line_length,
    )
    assert finder.find(index, 2) == 0


def test_has_adjacent_symbol_to_the_left_meme():
    assert has_adjacent_symbol(1, "^12", 3, 12) == 0

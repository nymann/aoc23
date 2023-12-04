from aoc23.day_03.finding_strategies.adjacent_above_finder import AdjacentAboveFinder
from aoc23.day_03.finding_strategies.adjacent_after_finder import AdjacentAfterFinder
from aoc23.day_03.finding_strategies.adjacent_before_finder import AdjacentBeforeFinder
from aoc23.day_03.finding_strategies.adjacent_below_finder import AdjacentBelowFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_above_left_finder import AdjacentDiagonalAboveLeftFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_above_right_finder import AdjacentDiagonalAboveRightFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_below_left_finder import AdjacentDiagonalBelowLeftFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_below_right_finder import AdjacentDiagonalBelowRightFinder
from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder


class AdjacentSymbolFinder:
    def __init__(self, puzzle_input: str, line_length: int) -> None:
        self._finders: list[AdjacentFinder] = []

        # Above
        self._finders.append(AdjacentAboveFinder(puzzle_input, line_length))
        self._finders.append(AdjacentDiagonalAboveLeftFinder(puzzle_input, line_length))
        self._finders.append(AdjacentDiagonalAboveRightFinder(puzzle_input, line_length))

        # Below
        self._finders.append(AdjacentBelowFinder(puzzle_input, line_length))
        self._finders.append(AdjacentDiagonalBelowLeftFinder(puzzle_input, line_length))
        self._finders.append(AdjacentDiagonalBelowRightFinder(puzzle_input, line_length))

        # Same line
        self._finders.append(AdjacentBeforeFinder(puzzle_input, line_length))
        self._finders.append(AdjacentAfterFinder(puzzle_input, line_length))

    def find(self, index: int, number: int) -> bool:
        number_len = len(str(number))
        for finder in self._finders:
            if finder.find(index, number_len):
                return True
        return False


def has_adjacent_symbol(index: int, puzzle_input: str, line_length: int, number: int) -> bool:
    finder = AdjacentSymbolFinder(puzzle_input=puzzle_input, line_length=line_length)
    return finder.find(index, number)

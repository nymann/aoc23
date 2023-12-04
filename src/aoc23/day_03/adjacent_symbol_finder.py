from aoc23.day_03.finding_strategies.adjacent_above_finder import AdjacentAboveFinder
from aoc23.day_03.finding_strategies.adjacent_after_finder import AdjacentAfterFinder
from aoc23.day_03.finding_strategies.adjacent_before_finder import AdjacentBeforeFinder
from aoc23.day_03.finding_strategies.adjacent_below_finder import AdjacentBelowFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_above_left_finder import AdjacentDiagonalAboveLeftFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_above_right_finder import AdjacentDiagonalAboveRightFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_below_left_finder import AdjacentDiagonalBelowLeftFinder
from aoc23.day_03.finding_strategies.adjacent_diagonal_below_right_finder import AdjacentDiagonalBelowRightFinder
from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder
from aoc23.day_03.finding_strategies.adjacent_finder import DefaultSymbolStrategy


class AdjacentSymbolFinder:
    def __init__(
        self,
        puzzle_input: str,
        line_length: int,
        symbol_strategy: DefaultSymbolStrategy = DefaultSymbolStrategy(),
    ) -> None:
        self._finders: list[AdjacentFinder] = []

        # Above
        self._finders.append(AdjacentAboveFinder(puzzle_input, line_length, symbol_strategy))
        self._finders.append(AdjacentDiagonalAboveLeftFinder(puzzle_input, line_length, symbol_strategy))
        self._finders.append(AdjacentDiagonalAboveRightFinder(puzzle_input, line_length, symbol_strategy))

        # Below
        self._finders.append(AdjacentBelowFinder(puzzle_input, line_length, symbol_strategy))
        self._finders.append(AdjacentDiagonalBelowLeftFinder(puzzle_input, line_length, symbol_strategy))
        self._finders.append(AdjacentDiagonalBelowRightFinder(puzzle_input, line_length, symbol_strategy))

        # Same line
        self._finders.append(AdjacentBeforeFinder(puzzle_input, line_length, symbol_strategy))
        self._finders.append(AdjacentAfterFinder(puzzle_input, line_length, symbol_strategy))

    def find(self, index: int, number: int) -> int | None:
        number_len = len(str(number))
        for finder in self._finders:
            res = finder.find(index, number_len)
            if res is not None:
                return res
        return None


def has_adjacent_symbol(index: int, puzzle_input: str, line_length: int, number: int) -> int | None:
    finder = AdjacentSymbolFinder(puzzle_input=puzzle_input, line_length=line_length)
    return finder.find(index, number)

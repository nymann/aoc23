from typing import Iterable

from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder


class AdjacentDiagonalBelowLeftFinder(AdjacentFinder):
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        if len(self.puzzle_input) > index + self.line_length - 1:
            yield index + self.line_length - 1

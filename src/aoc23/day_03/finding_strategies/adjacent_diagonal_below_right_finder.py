from typing import Iterable

from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder


class AdjacentDiagonalBelowRightFinder(AdjacentFinder):
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        if len(self.puzzle_input) > index + self.line_length + number_length:
            yield index + self.line_length + number_length

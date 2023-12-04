from typing import Iterable

from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder


class AdjacentDiagonalAboveLeftFinder(AdjacentFinder):
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        if index > self.line_length:
            yield index - self.line_length - 1

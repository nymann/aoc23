from typing import Iterable

from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder


class AdjacentDiagonalAboveRightFinder(AdjacentFinder):
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        if index + number_length - self.line_length > 0:
            yield index + number_length - self.line_length

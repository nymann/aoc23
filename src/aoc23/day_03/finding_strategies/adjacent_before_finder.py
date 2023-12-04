from typing import Iterable

from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder


class AdjacentBeforeFinder(AdjacentFinder):
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        line_position = index % self.line_length
        if line_position > 0:
            yield index - 1

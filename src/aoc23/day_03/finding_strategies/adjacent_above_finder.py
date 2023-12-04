from collections.abc import Iterable

from aoc23.day_03.finding_strategies.adjacent_finder import AdjacentFinder


class AdjacentAboveFinder(AdjacentFinder):
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        if index > self.line_length - 1:
            for i in range(number_length):
                yield index + i - self.line_length

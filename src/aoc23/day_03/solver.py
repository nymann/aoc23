from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
import re

from aoc23.day_03.adjacent_symbol_finder import AdjacentSymbolFinder
from aoc23.day_03.finding_strategies.adjacent_finder import DefaultSymbolStrategy
from aoc23.day_03.finding_strategies.adjacent_finder import GearSymbolStrategy


@dataclass
class IndexResult:
    symbol_index: int
    number: int


class Day03Solver:
    def __init__(self, text_file: str | Path) -> None:
        with open(text_file) as dataw:
            self._lines = dataw.read().splitlines()

    def p1(self) -> int:
        return sum(res.number for res in self._get_symbol_indexes(DefaultSymbolStrategy()))

    def p2(self) -> int:
        gears: dict[int, list[int]] = {}
        for res in self._get_symbol_indexes(GearSymbolStrategy()):
            if res.symbol_index not in gears:
                gears[res.symbol_index] = []
            gears[res.symbol_index].append(res.number)

        result = 0
        for numbers in gears.values():
            if len(numbers) != 2:
                continue
            result += numbers[0] * numbers[1]
        return result

    def _get_symbol_indexes(self, symbol_strategy: DefaultSymbolStrategy) -> Iterable[IndexResult]:
        line_length = len(self._lines[0])
        puzzle_input = "".join(self._lines)
        symbol_finder = AdjacentSymbolFinder(
            puzzle_input=puzzle_input,
            line_length=line_length,
            symbol_strategy=symbol_strategy,
        )
        for index, line in enumerate(self._lines):
            for match in re.finditer(r"\d+", line):
                number = match.group()
                start_index = match.start() + (line_length * index)
                symbol_index = symbol_finder.find(start_index, int(number))
                if symbol_index is not None:
                    yield IndexResult(symbol_index=symbol_index, number=int(number))

from pathlib import Path
import re

from aoc23.day_03.adjacent_symbol_finder import AdjacentSymbolFinder
from aoc23.day_03.finding_strategies.adjacent_finder import GearSymbolStrategy


class Day03Solver:
    def __init__(self, text_file: str | Path) -> None:
        with open(text_file) as dataw:
            self._lines = dataw.read().splitlines()

    def p1(self) -> int:
        data = self._lines
        line_length = len(data[0])
        puzzle_input = "".join(data)
        result = 0
        symbol_finder = AdjacentSymbolFinder(puzzle_input=puzzle_input, line_length=line_length)
        for index, line in enumerate(data):
            for match in re.finditer(r"\d+", line):
                number = match.group()
                start_index = match.start() + (line_length * index)
                if symbol_finder.find(start_index, int(number)) is not None:
                    result += int(number)

        return result

    def p2(self) -> int:
        data = self._lines
        gears: dict[int, list[int]] = {}
        line_length = len(data[0])
        puzzle_input = "".join(data)
        result = 0
        symbol_finder = AdjacentSymbolFinder(
            puzzle_input=puzzle_input,
            line_length=line_length,
            symbol_strategy=GearSymbolStrategy(),
        )
        for index, line in enumerate(data):
            for match in re.finditer(r"\d+", line):
                number = match.group()
                start_index = match.start() + (line_length * index)
                gear_index = symbol_finder.find(start_index, int(number))
                if gear_index is not None:
                    if gear_index not in gears:
                        gears[gear_index] = []
                    gears[gear_index].append(int(number))
        for gear_index, numbers in gears.items():
            if len(numbers) != 2:
                continue
            result += numbers[0] * numbers[1]

        return result

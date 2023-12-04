from pathlib import Path
import re

from aoc23.day_03.adjacent_symbol_finder import AdjacentSymbolFinder


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
                if int(number) == 690:
                    print(start_index)

                if symbol_finder.find(start_index, int(number)):
                    result += int(number)

        return result

    def p2(self) -> int:
        return 0

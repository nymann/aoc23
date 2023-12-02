from pathlib import Path

from aoc23.day_02.fewest_cubes_determiner import FewestCubesDeterminer
from aoc23.day_02.game_record_parser import GameRecordParser
from aoc23.day_02.game_record_parser import LineParser
from aoc23.day_02.game_validity_checker import GameValidityChecker


class Day2Solver:
    def __init__(self, input_file: Path | str) -> None:
        self._input_file = input_file
        self.parser = GameRecordParser(line_parser=LineParser())

    def p1(self, red: int, green: int, blue: int) -> int:
        valid_checker = GameValidityChecker(red=red, green=green, blue=blue)
        result = 0
        for game in self.parser.parse(self._input_file):
            if valid_checker.is_game_valid(game=game):
                result += game.game_id
        return result

    def p2(self) -> int:
        determiner = FewestCubesDeterminer()
        result = 0
        for game in self.parser.parse(self._input_file):
            minimum_cubes = determiner.determine(game=game)
            result += minimum_cubes.green * minimum_cubes.red * minimum_cubes.blue

        return result

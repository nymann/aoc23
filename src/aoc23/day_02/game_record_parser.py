from collections.abc import Iterable
from pathlib import Path

from aoc23.day_02.game import Game
from aoc23.day_02.game import GameSet


class LineParser:
    def parse(self, record: str) -> Game:
        colon_split = record.split(":", maxsplit=1)
        game_id = int(colon_split[0][4:])
        set_split = colon_split[1].split(";")
        game_sets = [self._extract_game_set(set_text) for set_text in set_split]
        return Game(sets=game_sets, game_id=game_id)

    def _extract_game_set(self, set_text: str) -> GameSet:
        game_set_dict: dict[str, int] = {}
        cubes = set_text.split(",")
        for cube in cubes:
            amount, color = cube.strip().split(" ")
            game_set_dict[color] = int(amount)
        return GameSet(**game_set_dict)


class GameRecordParser:
    def __init__(self, line_parser: LineParser) -> None:
        self._line_parser = line_parser

    def parse(self, input_file: str | Path) -> Iterable[Game]:
        with open(input_file, "r") as text_file:
            for line in text_file:
                yield self._line_parser.parse(record=line)

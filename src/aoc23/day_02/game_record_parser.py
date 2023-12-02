from collections.abc import Iterable
from pathlib import Path

from aoc23.day_02.game import Game
from aoc23.day_02.game import GameSet


class LineParser:
    def parse(self, record: str) -> Game:
        game_split = record.split(":", maxsplit=1)
        game_id = int(game_split[0][4:])
        set_split = game_split[1].split(";")
        game_sets: list[GameSet] = []
        for set_text in set_split:
            game_set_dict: dict[str, int] = {}
            cubes = set_text.split(",")
            for cube in cubes:
                amount, color = cube.strip().split(" ")
                game_set_dict[color] = int(amount)
            game_sets.append(GameSet(**game_set_dict))
        return Game(sets=game_sets, game_id=game_id)


class GameRecordParser:
    def __init__(self, line_parser: LineParser) -> None:
        self._line_parser = line_parser

    def parse(self, input_file: str | Path) -> Iterable[Game]:
        with open(input_file, "r") as text_file:
            for line in text_file:
                yield self._line_parser.parse(record=line)

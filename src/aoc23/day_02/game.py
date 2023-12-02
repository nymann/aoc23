from dataclasses import dataclass


@dataclass
class GameSet:
    red: int = 0
    blue: int = 0
    green: int = 0


@dataclass
class Game:
    sets: list[GameSet]
    game_id: int

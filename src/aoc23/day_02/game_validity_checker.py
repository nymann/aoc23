from aoc23.day_02.game import Game
from aoc23.day_02.game import GameSet


class GameValidityChecker:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    def is_game_valid(self, game: Game) -> bool:
        return all(self._is_set_valid(game_set) for game_set in game.sets)

    def _is_set_valid(self, game_set: GameSet) -> bool:
        return all(
            [
                game_set.blue <= self._blue,
                game_set.green <= self._green,
                game_set.red <= self._red,
            ],
        )

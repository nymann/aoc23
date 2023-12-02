from aoc23.day_02.game import Game
from aoc23.day_02.game import GameSet


class FewestCubesDeterminer:
    def determine(self, game: Game) -> GameSet:
        blue = 0
        green = 0
        red = 0
        for game_set in game.sets:
            blue = max(blue, game_set.blue)
            green = max(green, game_set.green)
            red = max(red, game_set.red)
        return GameSet(blue=blue, red=red, green=green)

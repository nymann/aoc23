from pathlib import Path

from aoc23.day_04.point_calculator import PointCalculator
from aoc23.day_04.scratch_card_parser import ScratchCardParser


class Day04Solver:
    def __init__(self, input_file: Path | str) -> None:
        self.lines = []
        with open(input_file, "r") as text_file:
            self.lines = text_file.readlines()

    def p1(self) -> int:
        parser = ScratchCardParser()
        point_calculator = PointCalculator()
        result = 0
        for line in self.lines:
            scratch_card = parser.parse(line)
            result += point_calculator.calculate(scratch_card)

        return result

    def p2(self) -> int:
        temp: dict[int, int] = {}
        parser = ScratchCardParser()
        result: dict[int, int] = {}
        for line in self.lines:
            scratch_card = parser.parse(line)
            amount = len(scratch_card.correct_numbers())
            if scratch_card.card_id not in temp:
                temp[scratch_card.card_id] = 1
            else:
                temp[scratch_card.card_id] += 1

            for _ in range(temp[scratch_card.card_id]):
                for i in range(amount):
                    card_id = i + scratch_card.card_id + 1
                    if card_id in temp:
                        temp[card_id] += 1
                    else:
                        temp[card_id] = 1
            if scratch_card.card_id in temp:
                result[scratch_card.card_id] = temp[scratch_card.card_id]
                del temp[scratch_card.card_id]

        return sum(x for x in result.values())

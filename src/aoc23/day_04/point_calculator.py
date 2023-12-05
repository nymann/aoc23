from aoc23.day_04.scratch_card import ScratchCard


class PointCalculator:
    def calculate(self, scratch_card: ScratchCard) -> int:
        amount = len(scratch_card.correct_numbers())
        if amount <= 2:
            return amount
        return 2 ** (amount - 1)

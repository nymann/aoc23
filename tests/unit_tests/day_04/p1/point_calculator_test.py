from aoc23.day_04.point_calculator import PointCalculator
from aoc23.day_04.scratch_card import ScratchCard


def test_one_correct():
    scratch_card = ScratchCard(
        winning_numbers={1, 2, 3},
        our_numbers={1},
        card_id=1,
    )
    point_calculator = PointCalculator()
    points = point_calculator.calculate(scratch_card)
    assert points == 1


def test_three_correct():
    scratch_card = ScratchCard(
        winning_numbers={1, 2, 3},
        our_numbers={1, 2, 3},
        card_id=1,
    )
    point_calculator = PointCalculator()
    points = point_calculator.calculate(scratch_card)
    assert points == 4

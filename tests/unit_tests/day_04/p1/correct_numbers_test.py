from aoc23.day_04.scratch_card import ScratchCard


def test_correct_numbers():
    scratch_card = ScratchCard(
        winning_numbers={1, 2, 3},
        our_numbers={1, 2, 4},
        card_id=1,
    )
    assert scratch_card.correct_numbers() == {1, 2}

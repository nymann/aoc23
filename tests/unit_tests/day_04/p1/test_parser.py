from aoc23.day_04.scratch_card_parser import ScratchCardParser

line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"


def test_scratch_card_parser_winning_numbers():
    expected = {41, 48, 83, 86, 17}
    parser = ScratchCardParser()
    scratch_card = parser.parse(line)
    assert scratch_card.winning_numbers == expected


def test_scratch_card_parser_our_numbers():
    expected = {83, 86, 6, 31, 17, 9, 48, 53}
    parser = ScratchCardParser()
    scratch_card = parser.parse(line)
    assert scratch_card.our_numbers == expected


def test_scratch_card_parser_game_id():
    expected = 1
    parser = ScratchCardParser()
    scratch_card = parser.parse(line)
    assert scratch_card.card_id == expected

from aoc23.day_03.finding_strategies.adjacent_after_finder import AdjacentAfterFinder


def test_690():
    puzzle_input = "..614..831..33.....*...........@....*398..&.....690*............183.........503..916..790................................*.....256....632..."
    line_length = len(puzzle_input)
    finder = AdjacentAfterFinder(
        puzzle_input=puzzle_input,
        line_length=line_length,
    )
    index = 48
    line_position = index % line_length
    assert line_length == 140
    assert line_position == index
    assert puzzle_input[index] == "6"
    assert finder.find(index, 3)

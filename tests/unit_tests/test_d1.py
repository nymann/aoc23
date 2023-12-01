from aoc23.main import day1


def test_day1():
    lines = []
    with open("tests/unit_tests/d1.txt") as f:
        lines = f.readlines()
    assert day1(lines) == 142

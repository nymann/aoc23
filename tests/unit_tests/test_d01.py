from aoc23.day_01.solver import Day1Solver


def test_p1() -> None:
    solver = Day1Solver(input_file="tests/data/d01_p1.example")
    assert solver.p1() == 142


def test_p2() -> None:
    solver = Day1Solver(input_file="tests/data/d01_p2.example")
    assert solver.p2() == 281

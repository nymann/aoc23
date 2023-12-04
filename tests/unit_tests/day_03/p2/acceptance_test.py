from aoc23.day_03.solver import Day03Solver


def test_acceptance_d03_p2():
    solver = Day03Solver("tests/data/d03.example")
    assert solver.p2() == 467835

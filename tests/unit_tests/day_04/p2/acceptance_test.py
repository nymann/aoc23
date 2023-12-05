from aoc23.day_04.solver import Day04Solver


def test_total_points_example_input():
    solver = Day04Solver("tests/data/d04.example")
    assert solver.p2() == 30

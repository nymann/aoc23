from aoc23.day_02.solver import Day2Solver


def test_d02_p1():
    solver = Day2Solver("tests/data/d02.example")
    assert solver.p1(red=12, green=13, blue=14) == 8


def test_d02_p2():
    solver = Day2Solver("tests/data/d02.example")
    assert solver.p2() == 2286

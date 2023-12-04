from aoc23.day_03.adjacent_symbol_finder import has_adjacent_symbol
from aoc23.day_03.solver import Day03Solver


def acceptance_test_d03_p1():
    solver = Day03Solver("tests/data/d03.example")
    assert solver.p1() == 4361


def test_has_adjacent_symbol_to_the_left():
    assert has_adjacent_symbol(1, "^12", 3, 12)


def test_has_adjacent_symbol_to_the_right():
    assert has_adjacent_symbol(0, "12^", 3, 12)


def test_has_adjacent_symbol_above():
    assert has_adjacent_symbol(3, "*..12.", 3, 12)


def test_has_shifted_adjacent_symbol_above():
    assert has_adjacent_symbol(3, ".*.12.", 3, 12)


def test_has_adjacent_symbol_below():
    assert has_adjacent_symbol(0, "1.*.", 2, 1)


def test_has_adjacent_symbol_below_alternate():
    assert has_adjacent_symbol(1, ".12..*..", 4, 12)


def test_has_shifted_adjacent_symbol_below():
    assert has_adjacent_symbol(0, "12..*.", 3, 12)


def test_diagonal_above_left():
    assert has_adjacent_symbol(4, "#...12", 3, 12)


def test_diagonal_above_right():
    assert has_adjacent_symbol(3, "..#12.", 3, 12)


def test_diagonal_below_left():
    assert has_adjacent_symbol(1, ".12.#...", 4, 12)


def test_diagonal_below_right():
    assert has_adjacent_symbol(1, ".12....#", 4, 12)

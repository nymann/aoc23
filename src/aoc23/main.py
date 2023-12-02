from pathlib import Path

import typer

from aoc23.day_02.solver import Day2Solver

app = typer.Typer()


@app.command()
def main(input_file: Path, red: int, green: int, blue: int) -> None:
    solver = Day2Solver(input_file=input_file)
    p1 = solver.p1(red=red, green=green, blue=blue)
    typer.echo(f"P1: '{p1}'")
    typer.echo(f"P2: '{solver.p2()}'")


if __name__ == "__main__":
    app()

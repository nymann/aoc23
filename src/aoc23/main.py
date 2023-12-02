from pathlib import Path

import typer

from aoc23.day_02.solver import Day2Solver

app = typer.Typer()


@app.command()
def main(input_file: Path) -> None:
    solver = Day2Solver(input_file=input_file)
    typer.echo(f"P1: '{solver.p1(red=12, green=13, blue=14)}'")
    typer.echo(f"P2: '{solver.p2()}'")


if __name__ == "__main__":
    app()

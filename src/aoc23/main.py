from pathlib import Path

import typer

from aoc23.day_04.solver import Day04Solver

app = typer.Typer()


@app.command()
def main(input_file: Path) -> None:
    solver = Day04Solver(input_file)
    typer.echo(f"P1: '{solver.p1()}'")
    typer.echo(f"P2: '{solver.p2()}'")


if __name__ == "__main__":
    app()

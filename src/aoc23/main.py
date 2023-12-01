from pathlib import Path
import re

import typer

app = typer.Typer()


@app.command()
def main(f: Path) -> None:
    res = 0
    with open(f) as file:
        res = day1(file.readlines())

    typer.echo(res)


def day1(lines: list[str]) -> int:
    return sum(calibrate_line(line) for line in lines)


def calibrate_line(line: str) -> int:
    digits = re.findall(r"\d", line)
    return int(f"{digits[0]}{digits[-1]}")


if __name__ == "__main__":
    app()

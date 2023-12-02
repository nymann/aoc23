from pathlib import Path

from aoc23.day_01.digit_extractor_strategies import DigitExtractor
from aoc23.day_01.digit_extractor_strategies import WordDigitExtractor
from aoc23.day_01.line_calibrator import LineCalibrator


class Day1Solver:
    def __init__(self, input_file: Path | str) -> None:
        self.lines = []
        with open(input_file, "r") as text_file:
            self.lines = text_file.readlines()

    def p1(self) -> int:
        line_calibrator = LineCalibrator(digit_finder_strategy=DigitExtractor())
        return self._sum_calibrated_lines(line_calibrator)

    def p2(self) -> int:
        line_calibrator = LineCalibrator(digit_finder_strategy=WordDigitExtractor())
        return self._sum_calibrated_lines(line_calibrator)

    def _sum_calibrated_lines(self, line_calibrator: LineCalibrator) -> int:
        return sum(line_calibrator.calibrate(line) for line in self.lines)

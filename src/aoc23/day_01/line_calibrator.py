from aoc23.day_01.digit_extractor_strategies import DigitExtractorStrategy


class LineCalibrator:
    def __init__(self, digit_finder_strategy: DigitExtractorStrategy) -> None:
        self.digit_finder_strategy = digit_finder_strategy

    def calibrate(self, line: str) -> int:
        return self.digit_finder_strategy.first(line) * 10 + self.digit_finder_strategy.last(line)

from abc import ABC
from abc import abstractmethod


class DigitExtractorStrategy(ABC):
    @abstractmethod
    def first(self, line: str) -> int:
        raise NotImplementedError

    @abstractmethod
    def last(self, line: str) -> int:
        raise NotImplementedError


class DigitExtractor(DigitExtractorStrategy):
    def first(self, line: str) -> int:
        return self._first_digit(line)

    def last(self, line: str) -> int:
        return self._first_digit(line[::-1])

    def _first_digit(self, line: str) -> int:
        for character in line:
            if character.isdigit():
                return int(character)
        raise RuntimeError(line)


class WordDigitExtractor(DigitExtractorStrategy):
    def __init__(self) -> None:
        self.digit_words = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        self.reversed_digit_words = {word[::-1]: digit for word, digit in self.digit_words.items()}  # noqa: WPS221

    def first(self, line: str) -> int:
        return self._find_digit(line, self.digit_words)

    def last(self, line: str) -> int:
        return self._find_digit(line[::-1], self.reversed_digit_words)

    def _find_digit(self, line: str, digit_words: dict[str, int]) -> int:
        for index, character in enumerate(line):
            if character.isdigit():
                return int(character)
            line_sub = line[index:]
            for word, digit in digit_words.items():
                if line_sub.startswith(word):
                    return digit
        raise RuntimeError(line)

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
        for character in line:
            if character.isdigit():
                return int(character)
        raise RuntimeError(line)

    def last(self, line: str) -> int:
        for character in line[::-1]:
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
        self.reversed_digit_words = {
            "eno": 1,
            "owt": 2,
            "eerht": 3,
            "ruof": 4,
            "evif": 5,
            "xis": 6,
            "neves": 7,
            "thgie": 8,
            "enin": 9,
        }

    def first(self, line: str) -> int:
        for index, character in enumerate(line):
            if character.isdigit():
                return int(character)
            line_sub = line[index:]
            for word, digit in self.digit_words.items():
                if line_sub.startswith(word):
                    return digit
        raise RuntimeError(line)

    def last(self, line: str) -> int:
        reversed_line = line[::-1]
        for index, character in enumerate(reversed_line):
            if character.isdigit():
                return int(character)
            for word, digit in self.reversed_digit_words.items():
                if reversed_line[index:].startswith(word):
                    return digit
        raise RuntimeError(line)

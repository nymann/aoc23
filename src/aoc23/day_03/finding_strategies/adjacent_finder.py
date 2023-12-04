from abc import ABC
from abc import abstractmethod
from typing import Iterable


class AdjacentFinder(ABC):
    def __init__(self, puzzle_input: str, line_length: int) -> None:
        self.puzzle_input = puzzle_input
        self.line_length = line_length

    def find(self, index: int, number_length: int) -> bool:
        for index_to_check in self._indexes_to_check(index=index, number_length=number_length):
            if self._is_symbol(index_to_check):
                return True
        return False

    @abstractmethod
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        raise NotImplementedError

    def _is_symbol(self, index: int) -> bool:
        chr = self.puzzle_input[index]
        if chr.isdigit():
            return False
        return chr != "."

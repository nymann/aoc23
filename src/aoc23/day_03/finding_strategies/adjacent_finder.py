from abc import ABC
from abc import abstractmethod
from typing import Iterable


class DefaultSymbolStrategy:
    def is_symbol(self, chr: str) -> bool:
        if chr.isdigit():
            return False
        return chr != "."


class GearSymbolStrategy(DefaultSymbolStrategy):
    def is_symbol(self, chr: str) -> bool:
        return chr == "*"


class AdjacentFinder(ABC):
    def __init__(
        self,
        puzzle_input: str,
        line_length: int,
        symbol_strategy: DefaultSymbolStrategy = DefaultSymbolStrategy(),
    ) -> None:
        self.puzzle_input = puzzle_input
        self.line_length = line_length
        self.symbol_strategy = symbol_strategy

    def find(self, index: int, number_length: int) -> int | None:
        for index_to_check in self._indexes_to_check(index=index, number_length=number_length):
            if self.symbol_strategy.is_symbol(self.puzzle_input[index_to_check]):
                return index_to_check
        return None

    @abstractmethod
    def _indexes_to_check(self, index: int, number_length: int) -> Iterable[int]:
        raise NotImplementedError

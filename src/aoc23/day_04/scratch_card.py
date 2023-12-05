from dataclasses import dataclass


@dataclass
class ScratchCard:
    winning_numbers: set[int]
    our_numbers: set[int]
    card_id: int

    def correct_numbers(self) -> set[int]:
        return self.our_numbers & self.winning_numbers

from aoc23.day_04.scratch_card import ScratchCard


class ScratchCardParser:
    def parse(self, line: str) -> ScratchCard:
        colon_split = line.split(":")
        card_id = int(colon_split[0][4:])
        winning_numbers_str, our_numbers_str = colon_split[1].split("|")
        winning_numbers = {int(winning_number) for winning_number in winning_numbers_str.split()}
        our_numbers = {int(our_number) for our_number in our_numbers_str.split()}
        return ScratchCard(
            winning_numbers=winning_numbers,
            our_numbers=our_numbers,
            card_id=card_id,
        )

from src.aoc7.camel_card_hand import CamelCardHand
from src.utils.input.input_line import InputLine


class CamelCardGame:

    def __init__(self, input_lines: [InputLine]):
        hands = [CamelCardHand(input_line.line_str, input_line.next_line_part) for input_line in input_lines]
        self.hands = sorted(hands)
        self.winnings_dict = self.calc_winnings_dict(self.hands)
        self.total_winnings = self.calc_total_winnings(self.winnings_dict)

    @staticmethod
    def calc_winnings_dict(hands: [CamelCardHand]):
        # { hand_str: (rank, bid, winnings) }
        winnings_dict: {str: (int, int, int)} = {}

        for i in range(0, len(hands)):
            rank = i + 1
            bid = hands[i].bid
            winnings = bid * rank
            winnings_dict[hands[i].hand_str] = (rank, bid, winnings)

        return winnings_dict

    @staticmethod
    def calc_total_winnings(winnings_dict: {str: (int, int, int)}):
        return sum(rank_bid_wins_tuple[2] for rank_bid_wins_tuple in winnings_dict.values())

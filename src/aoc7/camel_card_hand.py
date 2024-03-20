from src.aoc7 import *
from src.aoc7.camel_card import CamelCard
from src.utils.string_helper import char_count


class CamelCardHand:

    def __init__(self, hand_str: str, bid_str: str, joker_rule: bool = False):
        if hand_str is None:
            raise ValueError("The hand string cannot be None!\n")
        if len(hand_str) != 5:
            raise ValueError(f"The hand string needs to be exactly 5 chars long but str={hand_str}\n")
        if bid_str is None:
            raise ValueError("The bid string cannot be None!\n")

        self.bid = int(bid_str)
        self.hand_str = hand_str
        self.play_with_joker_rule = joker_rule
        self.cards = self._hand_cards(hand_str, joker_rule)
        self.joker_hand_str = self._use_jokers(hand_str, self.cards, joker_rule)
        self.hand_type = self._determine_type(self.joker_hand_str)
        self.hand_type_rank = self.type_rank_dict()[self.hand_type]

    def __lt__(self, other):
        return (((self.hand_type_rank,) + tuple(card.card_rank for card in self.cards)) <
                ((other.hand_type_rank,) + tuple(card.card_rank for card in other.cards)))

    @staticmethod
    def _hand_cards(hand_str: str, joker_rule: bool = False):
        return [CamelCard(char, joker_rule) for char in hand_str]

    @staticmethod
    def _use_jokers(hand_str: str, cards: [CamelCard], joker_rule: bool = False) -> str:
        joker = 'J'
        char_counts_dict = char_count(hand_str)

        if joker not in char_counts_dict or not joker_rule:
            return hand_str

        joker_count = char_counts_dict[joker]
        if joker_count == 5:
            return "AAAAA"

        no_joker_counts_dict = {key: value for key, value in char_counts_dict.items() if key != joker}

        if joker_count == 4:
            return hand_str.replace(joker, list(no_joker_counts_dict.keys())[0])

        no_joker_cards = [card for card in cards if card.card_label != joker]
        highest_rank_card = max(no_joker_cards, key=lambda card: card.card_rank)
        new_card_char = CamelCardHand._find_card_char_to_replace(no_joker_counts_dict, highest_rank_card.card_label)

        return hand_str.replace(joker, new_card_char)

    @staticmethod
    def _find_card_char_to_replace(no_joker_counts_dict: {str: int}, highest_rank_card_label: str) -> str:
        most_frequent_char = max(no_joker_counts_dict, key=lambda k: no_joker_counts_dict[k])

        if CamelCardHand._more_than_half(most_frequent_char, no_joker_counts_dict):
            return most_frequent_char

        return highest_rank_card_label

    @staticmethod
    def _more_than_half(most_frequent_char: str, no_joker_counts_dict: {str: int}) -> bool:
        most_frequent_char_count = no_joker_counts_dict[most_frequent_char]
        is_more_than_half = True
        for key, value in no_joker_counts_dict.items():
            if key != most_frequent_char:
                if value == most_frequent_char_count:
                    is_more_than_half = False
        return is_more_than_half

    @staticmethod
    def _determine_type(hand_str: str) -> str:
        hand_type_check_functions = {
            FIVE_KIND: CamelCardHand._is_five_kind,
            FOUR_KIND: CamelCardHand._is_four_kind,
            FULL_HOUSE: CamelCardHand._is_full_house,
            THREE_KIND: CamelCardHand._is_three_kind,
            TWO_PAIR: CamelCardHand._is_two_pair,
            ONE_PAIR: CamelCardHand._is_one_pair,
            HIGH_CARD: CamelCardHand._is_high_card
        }

        char_counts = char_count(hand_str)

        for current_hand_type, check_function in hand_type_check_functions.items():
            if check_function(char_counts):
                return current_hand_type

        raise Exception(f"No valid hand type could be found for the str: {hand_str} !\n")

    @staticmethod
    def type_rank_dict():
        return {FIVE_KIND: 7,
                FOUR_KIND: 6,
                FULL_HOUSE: 5,
                THREE_KIND: 4,
                TWO_PAIR: 3,
                ONE_PAIR: 2,
                HIGH_CARD: 1}

    @staticmethod
    def _is_five_kind(char_count_dict: {str: int}) -> bool:
        return 5 in char_count_dict.values()

    @staticmethod
    def _is_four_kind(char_count_dict: {str: int}) -> bool:
        return 4 in char_count_dict.values()

    @staticmethod
    def _is_full_house(char_count_dict: {str: int}) -> bool:
        counts = char_count_dict.values()
        return 3 in counts and 2 in counts

    @staticmethod
    def _is_three_kind(char_count_dict: {str: int}) -> bool:
        return 3 in char_count_dict.values()

    @staticmethod
    def _is_two_pair(char_count_dict: {str: int}) -> bool:
        pairs = [key for key, value in char_count_dict.items() if value == 2]
        return len(pairs) == 2

    @staticmethod
    def _is_one_pair(char_count_dict: {str: int}) -> bool:
        pairs = [key for key, value in char_count_dict.items() if value == 2]
        return len(pairs) == 1

    @staticmethod
    def _is_high_card(char_count_dict: {str: int}) -> bool:
        return all(count == 1 for count in char_count_dict.values())

import pytest

from src.aoc7 import *
from src.aoc7.camel_card_hand import CamelCardHand
from src.utils.string_helper import char_count


class TestCamelCardHand:

    @pytest.mark.parametrize("hand_str, bid_str, expected_hand_type, expected_hand_type_rank", [
        ("AAAAA", "1000", FIVE_KIND, 7),
        ("AA8AA", "1000", FOUR_KIND, 6),
        ("23332", "1000", FULL_HOUSE, 5),
        ("TTT98", "1000", THREE_KIND, 4),
        ("23432", "1000", TWO_PAIR, 3),
        ("A23A4", "1000", ONE_PAIR, 2),
        ("23456", "1000", HIGH_CARD, 1)
    ])
    def test_initialization(self, hand_str, bid_str, expected_hand_type, expected_hand_type_rank):
        card_hand = CamelCardHand(hand_str, bid_str)
        assert card_hand.hand_str == hand_str
        assert card_hand.bid == int(bid_str)
        assert card_hand.hand_type == expected_hand_type
        assert card_hand.hand_type_rank == expected_hand_type_rank

    @pytest.mark.parametrize("hand_str, expected", [
        ("AAAAA", FIVE_KIND),
        ("AA8AA", FOUR_KIND),
        ("23332", FULL_HOUSE),
        ("TTT98", THREE_KIND),
        ("23432", TWO_PAIR),
        ("A23A4", ONE_PAIR),
        ("23456", HIGH_CARD)
    ])
    def test_determine_type(self, hand_str, expected):
        assert CamelCardHand._determine_type(hand_str) == expected

    @pytest.mark.parametrize("hand_str, expected", [
        ("AAAAA", True),
        ("4AAAA", False),
        ("12345", False)
    ])
    def test_is_five_kind(self, hand_str, expected):
        assert CamelCardHand._is_five_kind(char_count(hand_str)) == expected

    @pytest.mark.parametrize("hand_str, expected", [
        ("11AAA", False),
        ("4AAAA", True),
        ("AAAA4", True),
        ("12345", False),
        ("AA8AA", True)
    ])
    def test_is_four_kind(self, hand_str, expected):
        assert CamelCardHand._is_four_kind(char_count(hand_str)) == expected

    @pytest.mark.parametrize("hand_str, expected", [
        ("23332", True),
        ("21332", False),
        ("BBAAA", True),
        ("33232", True),
        ("25A3B", False)
    ])
    def test_is_full_house(self, hand_str, expected):
        assert CamelCardHand._is_full_house(char_count(hand_str)) == expected

    @pytest.mark.parametrize("hand_str, expected", [
        ("11AAA", True),
        ("4AAAA", False),
        ("AAA44", True),
        ("12345", False),
        ("TTT98", True)

    ])
    def test_is_three_kind(self, hand_str, expected):
        assert CamelCardHand._is_three_kind(char_count(hand_str)) == expected

    @pytest.mark.parametrize("hand_str, expected", [
        ("11AAA", False),
        ("11A11", False),  # This is technically also two pairs but should be covered by 4 of a kind
        ("23432", True),
        ("AAA14", False),
        ("12345", False),
        ("23432", True)
    ])
    def test_is_two_pair(self, hand_str, expected):
        assert CamelCardHand._is_two_pair(char_count(hand_str)) == expected

    @pytest.mark.parametrize("hand_str, expected", [
        ("11AAA", True),
        ("11A2B", True),
        ("11A11", False),
        ("AAA14", False),
        ("12345", False)
    ])
    def test_is_one_pair(self, hand_str, expected):
        assert CamelCardHand._is_one_pair(char_count(hand_str)) == expected

    @pytest.mark.parametrize("hand_str, expected", [
        ("AA234", False),
        ("23456", True)
    ])
    def test_is_high_card(self, hand_str, expected):
        assert CamelCardHand._is_high_card(char_count(hand_str)) == expected

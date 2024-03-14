import random

import pytest

from src.aoc7.camel_card import CamelCard


class TestCamelCard:

    @pytest.mark.parametrize("input_label, expected_rank", [("A", 13)])
    def test_initialization(self, input_label, expected_rank):
        camel_card = CamelCard(input_label)
        assert camel_card.card_label == input_label
        assert camel_card.card_rank == expected_rank

    @pytest.mark.parametrize("camel_label_list, expected_sorted_list", [
        (['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'],
         ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])
    ])
    def test_sort_camel_cards(self, camel_label_list, expected_sorted_list):
        random.shuffle(camel_label_list)
        camel_cards = [CamelCard(label) for label in camel_label_list]
        sorted_labels = [card.card_label for card in sorted(camel_cards)]
        assert sorted_labels == expected_sorted_list

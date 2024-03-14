from dataclasses import dataclass


@dataclass(frozen=True)
class HandType:
    FIVE_KIND = "Five of a kind"
    FOUR_KIND = "Four of a kind"
    FULL_HOUSE = "Full House"
    THREE_KIND = "Three of a kind"
    TWO_PAIR = "Two pair"
    ONE_PAIR = "One pair"
    HIGH_CARD = "High card"

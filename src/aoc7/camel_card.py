class CamelCard:

    def __init__(self, card_label: str, joker_rule: bool = False):
        if card_label is None:
            raise ValueError("Card label cannot be None!\n")
        if len(card_label) != 1:
            raise ValueError(f"The card label needs to be exactly one char but this.card_label = {card_label}\n")

        self.card_label = card_label
        if not joker_rule:
            self.card_rank = CamelCard.card_rank_dict()[card_label]
        else:
            self.card_rank = CamelCard.joker_card_rank_dict()[card_label]

    @staticmethod
    def card_rank_dict() -> {str: int}:
        return {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2,
                "2": 1}

    @staticmethod
    def joker_card_rank_dict() -> {str: int}:
        return {"A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
                "2": 2, "J": 1}

    def __lt__(self, other):
        return self.card_rank < other.card_rank

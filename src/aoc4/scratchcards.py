from src.aoc4.card import Card


class Scratchcards:

    def __init__(self, cards_list: [Card]):
        if cards_list is None:
            raise ValueError("The list of cards is None!!")

        self.m_cards_list = cards_list
        self._generate_card_dict(cards_list)
        self._process_scratchcards()
        self._calc_total_scratchcards()

    def _generate_card_dict(self, cards_list: [Card]):
        # {card_id: (Card, Copies Count, Allowed to add copies)}
        self.card_count_dict: {int: (Card, int, True)} = {card.card_id: (card, 1, True) for card in cards_list}
        self.max_id = max(cards_list, key=lambda card: card.card_id).card_id

    def _calc_total_scratchcards(self):
        self.total_cards = sum(triple[1] for triple in self.card_count_dict.values())

    def _process_scratchcards(self):
        for current_card_id in sorted(self.card_count_dict.keys()):
            # Once a card is processed it's no longer eligible for copies
            self._disallow_copies(current_card_id)
            current_card: [Card] = self.card_count_dict[current_card_id][0]
            current_card_copies_count = self.card_count_dict[current_card_id][1]
            for _ in range(current_card_copies_count):
                self._add_copies(current_card_id, self._calc_copies(current_card_id, current_card.matches_count))

    def _add_copies(self, current_card_id: int, copy_ids: [int]):
        for card_id in copy_ids:
            self._increase_copy_count(current_card_id, card_id)

    def _increase_copy_count(self, current_card_id: int, card_id_to_increase: int):
        if self._adding_copies_allowed(card_id_to_increase):
            triple = self.card_count_dict[card_id_to_increase]
            new_card_instances_count = triple[1] + 1
            self.card_count_dict[card_id_to_increase] = (triple[0], new_card_instances_count, triple[2])

    def _disallow_copies(self, card_id: int):
        triple = self.card_count_dict[card_id]
        self.card_count_dict[card_id] = (triple[0], triple[1], False)

    def _calc_copies(self, current_id: int, match_count: int):
        """
        returns a list with the card id's of copies
        """
        copies = []
        if match_count == 0:
            return copies

        for copy_id in range(current_id, current_id + match_count + 1):
            if self._adding_copies_allowed(copy_id):
                copies.append(copy_id)

        return copies

    def _id_exist(self, id_to_check: int):
        if self.card_count_dict.get(id_to_check) is not None:
            return True
        return False

    def _adding_copies_allowed(self, id_to_check: int):
        if self._id_exist(id_to_check):
            return self.card_count_dict[id_to_check][2]
        return False

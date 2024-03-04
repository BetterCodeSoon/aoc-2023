import re

from src.utils.string_helper import to_int
from utils.input.input_line import InputLine


class Card:

    def __init__(self, input_line: InputLine):
        self.game_id: int = int(self._remove_non_digits(input_line.line_str))
        self._split_numbers(input_line.next_line_part)
        self._card_points()

    def _split_numbers(self, input_str):
        card_numbers_line = InputLine(input_str, "|")
        self.winning_numbers = to_int(card_numbers_line.line_str.lstrip().split(" "))
        self.card_numbers = to_int(card_numbers_line.next_line_part.lstrip().split(" "))

    @staticmethod
    def _remove_non_digits(input_str):
        return re.sub(r'\D', '', input_str)

    @staticmethod
    def _points(number_of_matches, current_points):
        if number_of_matches == 1:
            return 1
        return current_points * 2

    def _card_points(self):
        self.points = 0
        self.matches = 0

        if len(self.winning_numbers) != 0:

            for winning_num in self.winning_numbers:
                if winning_num in self.card_numbers:
                    self.matches += 1
                    self.points = self._points(self.matches, self.points)

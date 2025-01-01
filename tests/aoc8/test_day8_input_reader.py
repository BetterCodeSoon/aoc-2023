import pytest

from src.aoc8.day8_input_reader import Day8InputReader
from src.utils.input.testcase_input_file import TestcaseInputFile


class TestDay8InputReader:
    testcases_file1 = TestcaseInputFile(8, 1)

    @pytest.mark.parametrize(["expected_path", "expected_network_dict"],
                             [
                                 ("RL", {'AAA': ('BBB', 'CCC'),
                                         'BBB': ('DDD', 'EEE'),
                                         'CCC': ('ZZZ', 'GGG'),
                                         'DDD': ('DDD', 'DDD'),
                                         'EEE': ('EEE', 'EEE'),
                                         'GGG': ('GGG', 'GGG'),
                                         'ZZZ': ('ZZZ', 'ZZZ')})
                             ])
    def test_initialization(self, expected_path, expected_network_dict):
        day8_input_reader = Day8InputReader(self.testcases_file1)
        assert day8_input_reader.path == expected_path
        assert day8_input_reader.network_dict == expected_network_dict

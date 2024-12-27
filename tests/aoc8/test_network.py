from src.aoc8.day8_input_reader import Day8InputReader
from src.aoc8.network import Network
from src.utils.input.testcase_input_file import TestcaseInputFile

import pytest


class TestNetwork:
    testcases_file1 = TestcaseInputFile(8, 1, '#')
    testcases_file1_reader = Day8InputReader(testcases_file1)
    test1_network_dict = testcases_file1_reader.network_dict
    test1_path = testcases_file1_reader.path

    testcases_file2 = TestcaseInputFile(8, 2, '#')
    testcases_file2_reader = Day8InputReader(testcases_file2)
    test2_network_dict = testcases_file2_reader.network_dict
    test2_path = testcases_file2_reader.path

    @pytest.mark.parametrize(["expected_path", "expected_network_dict"],
                             [("RL",
                               {"AAA": ("BBB", "CCC"),
                                "BBB": ("DDD", "EEE"),
                                "CCC": ("ZZZ", "GGG"),
                                "DDD": ("DDD", "DDD"),
                                "EEE": ("EEE", "EEE"),
                                "GGG": ("GGG", "GGG"),
                                "ZZZ": ("ZZZ", "ZZZ")})])
    def test_initialization(self, expected_path, expected_network_dict):
        network = Network(self.test1_path, self.test1_network_dict)
        assert network.path == expected_path
        assert network.network_dict == expected_network_dict

    @pytest.mark.parametrize("path, network_dict, expected_count",
                             [(test1_path, test1_network_dict, 2),
                              (test2_path, test2_network_dict, 6)])
    def test_steps_to_zzz(self, path, network_dict, expected_count):
        assert Network(path, network_dict).part1_steps_to_zzz() == expected_count

    @pytest.mark.parametrize("path, start_node, expected_node, expected_count",
                             [("LR", "AAA", "EEE", 2),
                              ("RL", "AAA", "ZZZ", 2)])
    def test_run_path(self, path, start_node, expected_node, expected_count):
        network = Network(self.test1_path, self.test1_network_dict)
        assert network._part1_run_path(path, self.test1_network_dict, start_node) == expected_node
        assert network.part1_steps_counted == expected_count

    @pytest.mark.parametrize("direction_char, current_node, expected_node",
                             [("L", "AAA", "BBB"),
                              ("R", "AAA", "CCC")])
    def test_next_node(self, direction_char, current_node, expected_node):
        assert Network._next_node(self.test1_network_dict, direction_char, current_node) == expected_node

    @pytest.mark.parametrize("node_tuple, expected", [(("DDD", "EEE"), "EEE")])
    def test_right(self, node_tuple, expected):
        assert Network._right(node_tuple) == expected

    @pytest.mark.parametrize("node_tuple, expected", [(("DDD", "EEE"), "DDD")])
    def test_left(self, node_tuple, expected):
        assert Network._left(node_tuple) == expected

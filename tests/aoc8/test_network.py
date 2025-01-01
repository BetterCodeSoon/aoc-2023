import pytest

from src.aoc8.day8_input_reader import Day8InputReader
from src.aoc8.network import Network
from src.utils import benchmark_helper
from src.utils.input.testcase_input_file import TestcaseInputFile


class TestNetwork:
    testcases_file1 = TestcaseInputFile(8, 1, '#')
    testcases_file1_reader = Day8InputReader(testcases_file1)
    test1_network_dict = testcases_file1_reader.network_dict
    test1_path = testcases_file1_reader.path

    testcases_file2 = TestcaseInputFile(8, 2, '#')
    testcases_file2_reader = Day8InputReader(testcases_file2)
    test2_network_dict = testcases_file2_reader.network_dict
    test2_path = testcases_file2_reader.path

    testcases_file3 = TestcaseInputFile(8, 3, '#')
    testcases_file3_reader = Day8InputReader(testcases_file3)
    test3_network_dict = testcases_file3_reader.network_dict
    test3_path = testcases_file3_reader.path

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
        assert network.current_nodes == ["AAA"]
        assert network.counter.count == 0

    @pytest.mark.parametrize("network_dict, expected_starting_nodes",
                             [({"AAA": ("BBB", "CCC"),
                                "BBA": ("DDD", "EEE"),
                                "CCC": ("ZZZ", "GGG"),
                                "DAD": ("DDD", "DDD"),
                                "AEE": ("EEE", "EEE"),
                                "GGA": ("GGG", "GGG"),
                                "ZZZ": ("ZZZ", "ZZZ")}, ["AAA", "BBA", "GGA"])])
    def test_find_starting_nodes(self, network_dict, expected_starting_nodes):
        assert Network._find_starting_nodes(network_dict) == expected_starting_nodes

    @pytest.mark.parametrize("path, network_dict, expected_count",
                             [(test1_path, test1_network_dict, 2),
                              (test3_path, test3_network_dict, 6)])
    def test_part_calculations_and_benchmark(self, path, network_dict, expected_count):
        network = Network(path, network_dict)
        assert benchmark_helper.benchmark(network.calc_part2_iterative) == expected_count
        network._reset_part2_attributes()
        assert benchmark_helper.benchmark(network.calc_part2_brute_force_processpool) == expected_count
        network._reset_part2_attributes()
        assert benchmark_helper.benchmark(network.calc_part2_brute_force_threadpool) == expected_count
        network._reset_part2_attributes()
        assert benchmark_helper.benchmark(network.calc_part2_analytic) == expected_count

    @pytest.mark.parametrize("path, network_dict, expected_nodes, expected_count",
                             [("RL", test1_network_dict, ["ZZZ"], 2),
                              ("LRLRLR", test3_network_dict, ["11Z", "22Z"], 6)])
    def test_run_all_paths(self, path, network_dict, expected_nodes, expected_count):
        network = Network(path, network_dict)
        network._run_all_paths(network.current_nodes)
        assert network.current_nodes == expected_nodes
        assert network.counter.count == expected_count

    @pytest.mark.parametrize("direction_char, nodes, expected",
                             [("L", ["BBB", "CCC"], ["DDD", "ZZZ"]),
                              ("R", ["BBB", "CCC"], ["EEE", "GGG"])])
    def test_next_nodes(self, direction_char, nodes, expected):
        number_of_nodes = len(nodes)
        assert Network._next_nodes(self.test1_network_dict, direction_char, number_of_nodes, nodes) == expected

    @pytest.mark.parametrize("node, expected",
                             [("AAA", False),
                              ("AAZ", True)])
    def test_is_z_node(self, node, expected):
        assert Network._is_z_node(node) == expected

    @pytest.mark.parametrize("nodes, expected",
                             [(["AAA", "BBZ"], False),
                              (["AAZ", "BBZ"], True)])
    def test_all_are_z_nodes(self, nodes, expected):
        assert Network._are_all_z_nodes(nodes) == expected

    @pytest.mark.parametrize("path, network_dict, expected_count",
                             [(test1_path, test1_network_dict, 2),
                              (test2_path, test2_network_dict, 6)])
    def test_steps_to_zzz(self, path, network_dict, expected_count):
        assert Network(path, network_dict).part1_steps_to_zzz() == expected_count

    @pytest.mark.parametrize("path, start_node, expected_node, expected_count",
                             [("RL", "AAA", "ZZZ", 2)])
    def test_run_path_threadpool(self, path, start_node, expected_node, expected_count):
        assert Network._run_path_threadpool(path, self.test1_network_dict, start_node) == expected_count

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

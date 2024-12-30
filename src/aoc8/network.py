from src.utils.input.counter import Counter

ZZZ = "ZZZ"


class Network:

    def __init__(self, path: str, network_dict: {str: (str, str)}):
        self.path = path
        self.network_dict = network_dict
        # Part1 Solution attributes
        self.part1_steps_counted = 0
        self.part1_current_node = "AAA"
        # Part2 Solution attributes
        self.current_nodes: [str] = Network._find_starting_nodes(self.network_dict)
        self.counter = Counter()

    @staticmethod
    def _find_starting_nodes(network_dict: {str: (str, str)}) -> [str]:
        # Find all nodes that end with "A"
        return [node for node in network_dict.keys() if node[2] == "A"]

    def part2_calc_steps(self, verbose: bool = False):
        while not Network._are_all_z_nodes(self.current_nodes):
            count = self.counter.count
            if count == 0 and verbose:
                print(f"Starting to count steps.. \n\n")
            if count % 1000 == 0 and verbose:
                print(f"{count} steps.. \n")
            self.current_nodes = self._run_all_paths(self.current_nodes)
        print(f"Done counting steps at {self.counter.count}")

    def _run_all_paths(self, current_nodes: [str]) -> [str]:
        number_of_nodes = len(current_nodes)
        for direction_char in self.path:
            if Network._are_all_z_nodes(current_nodes):
                return current_nodes
            current_nodes = self._next_nodes(self.network_dict, direction_char, number_of_nodes, current_nodes)
            self.counter.count_up()
        return current_nodes

    @staticmethod
    def _next_nodes(network_dict: {str: (str, str)}, direction_char: str, number_of_nodes: int,
                    current_nodes: [str]) -> [str]:
        for i in range(0, number_of_nodes):
            current_nodes[i] = Network._next_node(network_dict, direction_char, current_nodes[i])
        return current_nodes

    @staticmethod
    def _next_node(network_dict: {str: (str, str)}, direction_char: str, current_node: str):
        return network_dict[current_node][0 if direction_char == "L" else 1]

    @staticmethod
    def _is_z_node(node_str: str) -> bool:
        return node_str[2] == "Z"

    @staticmethod
    def _are_all_z_nodes(nodes: [str]) -> bool:
        return all([Network._is_z_node(node_str) for node_str in nodes])

    def part1_steps_to_zzz(self) -> int:
        # follow sequence of instructions in path
        # IF final node equals ZZZ stop counting steps
        # ELSE run sequence again
        self.part1_current_node = self._part1_run_path(self.path, self.network_dict, self.part1_current_node)
        if self.part1_current_node == ZZZ:
            return self.part1_steps_counted
        else:
            return self.part1_steps_to_zzz()

    def _part1_run_path(self, path: str, network_dict: {str: (str, str)}, start_node: str) -> str:
        current_node = start_node
        for direction_char in path:
            if current_node == ZZZ:
                return current_node
            current_node = Network._next_node(network_dict, direction_char, current_node)
            self.part1_steps_counted += 1
        return current_node

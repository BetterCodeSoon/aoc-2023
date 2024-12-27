ZZZ = "ZZZ"


class Network:

    def __init__(self, path: str, network_dict: {str: (str, str)}):
        self.path = path
        self.network_dict = network_dict
        self.part1_steps_counted = 0
        self.current_node = "AAA"

    def part1_steps_to_zzz(self) -> int:
        # follow sequence of instructions in path
        # IF final node equals ZZZ stop counting steps
        # ELSE run sequence again
        self.current_node = self._part1_run_path(self.path, self.network_dict, self.current_node)
        if self.current_node == ZZZ:
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

    @staticmethod
    def _next_node(network_dict: {str: (str, str)}, direction_char: str, current_node: str):
        if direction_char == "L":
            return Network._left(network_dict[current_node])
        return Network._right(network_dict[current_node])

    @staticmethod
    def _left(node_tuple: (str, str)) -> str:
        return node_tuple[0]

    @staticmethod
    def _right(node_tuple: (str, str)) -> str:
        return node_tuple[1]

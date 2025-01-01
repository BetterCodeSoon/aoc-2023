from src.utils.input.input_file import InputFile


class Day8InputReader:
    def __init__(self, input_file: InputFile):
        if input_file is None:
            raise ValueError("Danger eek! The input file is None!!\n")

        self.path = input_file.file_lines[0]
        # last line in testfiles has expected path yield, remove -1 after debug
        node_lines = input_file.file_lines[2:]

        self.nodes = [self._extract_node_str_list(line_str) for line_str in node_lines]
        self.network_dict = dict((node[0], (node[1], node[2])) for node in self.nodes)

    @staticmethod
    def _extract_node_str_list(line_str: str) -> [str]:
        """
        Turn "RJK = (DPP, JQR)" into ["RJK", "DPP", "JQR"]
        """
        return line_str.replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()

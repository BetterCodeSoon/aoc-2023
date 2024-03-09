class SourceDestinationMap:

    def __init__(self, map_str: [str]):
        if map_str is None:
            raise ValueError("The list containing the maps is None!\n")

        self.map_name = map_str[0]
        self.source_name, self.destination_name = self._source_destination_names(map_str[0])
        # (source_range_start, dest_range_start, range_length,source_range_end, dest_range_end)
        self.src_to_dest_list: [(int, int, int, int, int)] = self._generate_mapping_from_ranges_list(map_str[1:])

    def destination_number(self, source_number: int) -> int:
        if source_number is None:
            raise ValueError("Cannot look up destination number for None key!\n")

        # if source_num in range of mapped_src_start or mapped_src_end calc the number
        # otherwise return same destination as source
        return self._mapped_dest_number(source_number, self.src_to_dest_list)

    @staticmethod
    def _mapped_dest_number(source_number: int, src_to_dest_list):
        for range_tuple in src_to_dest_list:
            source_start = range_tuple[0]
            source_end = range_tuple[3]
            destination_start = range_tuple[1]

            if source_start <= source_number <= source_end:
                diff = source_number - source_start
                return destination_start + diff

        return source_number

    @staticmethod
    def _source_destination_names(source_dest_str: str):
        return source_dest_str.split("-to-")

    @staticmethod
    def _process_range_line_str(line: str):
        return [int(elem) for elem in line.split(" ")]

    @staticmethod
    def _generate_mapping_from_line(range_list: [int]) -> (int, int, int, int, int):
        if range_list is None:
            raise ValueError("Cannot generate mapping for range list that is None!\n")

        if len(range_list) != 3:
            raise ValueError("The range list needs to have EXACTLY three elements!\n")

        dest_range_start = range_list[0]
        source_range_start = range_list[1]
        range_length = range_list[2]

        return (source_range_start, dest_range_start, range_length,
                source_range_start + range_length - 1, dest_range_start + range_length - 1)

    @staticmethod
    def _generate_mapping_from_ranges_list(ranges_str_list: [str]) -> [(int, int, int, int, int)]:
        if ranges_str_list is None:
            raise ValueError("Cannot generate mapping for map list that is None!\n")

        src_to_dest_list: [(int, int, int, int, int)] = []
        for range_line in ranges_str_list:
            src_to_dest_list.append(
                SourceDestinationMap._generate_mapping_from_line(
                    SourceDestinationMap._process_range_line_str(range_line)))

        return src_to_dest_list

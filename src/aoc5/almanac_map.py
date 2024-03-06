class AlmanacMap:

    def __init__(self, map_str: [str]):
        if map_str is None:
            raise ValueError("The list containing the maps is None!\n")

        self.map_name = map_str[0]
        self.source_name, self.destination_name = self._source_destination_names(map_str[0])
        self.src_to_dest_dict: {int: int} = self._generate_mapping_from_ranges_list(map_str[1:])

    def destination_number(self, source_number: int) -> int:
        if source_number is None:
            raise ValueError("Cannot look up destination number for None key!\n")
        if source_number in self.src_to_dest_dict:
            # return specific mapping if it exists
            return self.src_to_dest_dict[source_number]
        # otherwise return same destination as source
        return source_number

    @staticmethod
    def _source_destination_names(source_dest_str: str):
        return source_dest_str.split("-to-")

    @staticmethod
    def _process_range_line_str(line: str):
        return [int(elem) for elem in line.split(" ")]

    @staticmethod
    def _generate_mapping_from_line(range_list: [int]) -> {int: int}:
        if range_list is None:
            raise ValueError("Cannot generate mapping for range list that is None!\n")

        if len(range_list) != 3:
            raise ValueError("The range list needs to have EXACTLY three elements!\n")

        dest_range_start = range_list[0]
        source_range_start = range_list[1]
        range_length = range_list[2]

        dest_range_end = dest_range_start + range_length
        source_range_end = source_range_start + range_length

        src_to_dest_dict = {}

        for sourc_index, dest_index in zip(range(source_range_start, source_range_end), range(
                dest_range_start, dest_range_end)):
            src_to_dest_dict[sourc_index] = dest_index

        return src_to_dest_dict

    @staticmethod
    def _generate_mapping_from_ranges_list(ranges_str_list: [str]):
        if ranges_str_list is None:
            raise ValueError("Cannot generate mapping for map list that is None!\n")

        src_to_dest_dict: {int: int} = {}
        for range_line in ranges_str_list:
            src_to_dest_dict.update(
                AlmanacMap._generate_mapping_from_line(AlmanacMap._process_range_line_str(range_line)))

        return src_to_dest_dict

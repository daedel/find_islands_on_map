from typing import TextIO


def read_map_file(file_name="input.txt") -> TextIO:
    with open(file_name, "r") as map_file:
        for row, line in enumerate(map_file):
            line = list(line.strip())
            yield row, line

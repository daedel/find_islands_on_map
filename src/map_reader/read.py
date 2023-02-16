from typing import TextIO


def read_map_file(file_name='input.txt') -> TextIO:
    try:
        return open(file_name, 'r')
    except FileNotFoundError:
        print("File does not exist")
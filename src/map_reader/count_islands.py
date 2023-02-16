from typing import Tuple, List
from .read import read_map_file


class Island:

    def __init__(self, starting_points: List[Tuple[int, int]]):
        self._points: List[Tuple] = starting_points

    def get_points(self):
        return self._points

    def add_points(self, points: List[Tuple[int, int]]):
        self._points.extend(points)


class IslandCounter:
    islands: List[Island] = []

    @property
    def island_count(self):
        return len(self.islands)

    def add_island(self, points: List[Tuple[int, int]]):
        for row, col in points:
            if island_neighbor := self._get_neighbor(row, col):
                island_neighbor.add_points(points)
                return

        self.islands.append(Island(points))

    def _get_neighbor(self, row: int, col: int):
        for island in self.islands[::-1]:
            if self._check_if_island_is_next_to_point(island, row, col):
                return island
        return None

    @staticmethod
    def _check_if_island_is_next_to_point(island: Island, row: int, col: int):
        for x, y in island.get_points()[::-1]:
            if row - 1 == x and col - 1 == y:
                return True
            if row - 1 == x and col == y:
                return True
            if row - 1 == x and col + 1 == y:
                return True
            if row == x and col - 1 == y:
                return True
            if row == x and col + 1 == y:
                return True
            if row + 1 == x and col - 1 == y:
                return True
            if row + 1 == x and col + 1 == y:
                return True
            if row + 1 == x and col == y:
                return True
        return False

def get_all_islands_next_to(col, line):
    try:
        if line[col] == "0":
            return col
    except IndexError:
        return col

    line[col] = '#'
    return get_all_islands_next_to(col + 1, line)


def count_islands(path_to_file: str):
    island_counter = IslandCounter()
    map_file = read_map_file(path_to_file)
    for row, line in enumerate(map_file):
        line = list(line.strip())
        num_cols = len(line)
        for col in range(num_cols):
            if line[col] == "#":
                continue

            if line[col] == "1":
                points = [(row, col + point_nr) for point_nr in range(get_all_islands_next_to(col, line) - col)]
                island_counter.add_island(points)


    map_file.close()
    return island_counter.island_count
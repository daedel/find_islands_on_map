from typing import Tuple, List, Set
from .read import read_map_file


class Island:
    def __init__(self, starting_points: List[Tuple[int, int]]) -> None:
        self._points: List[Tuple] = starting_points

    def get_points(self) -> List[Tuple]:
        return self._points

    def add_points(self, points: List[Tuple[int, int]]) -> None:
        self._points.extend(points)


class IslandCounter:
    def __init__(self):
        self.islands: List[Island] = []
        self.island_count = 0

    def remove_all_islands(self):
        self.islands = []

    def add_island(self, points: List[Tuple[int, int]]) -> None:
        neighbors = []
        for row, col in points:
            neighbors.extend(self._get_neighbors(row, col))

        neighbors = set(neighbors)

        if len(neighbors) == 1:
            next(iter(neighbors)).add_points(points)
            return

        if len(neighbors) > 1:
            # create new island from old sub islands
            self._merge_sub_islands(neighbors, points)
            return

        self._insert_island(Island(points))

    def _merge_sub_islands(
        self, sub_islands: Set[Island], new_points: List[Tuple[int, int]]
    ) -> None:
        new_island = Island(
            [point for sub_island in sub_islands for point in sub_island.get_points()]
        )
        new_island.add_points(new_points)
        self._insert_island(new_island)

        # remove sub islands
        for sub_island in sub_islands:
            self._remove_island(sub_island)

    def _remove_island(self, island: Island) -> None:
        try:
            self.islands.remove(island)
        except ValueError:
            print(
                f"{island} is not self.islands list. in This should not happend!. Exiting!"
            )
            exit(0)
        self.island_count -= 1

    def _insert_island(self, island: Island) -> None:
        self.islands.append(island)
        self.island_count += 1

    def _get_neighbors(self, row: int, col: int) -> List[Island]:
        neighbors = []
        for island in self.islands[::-1]:
            if (
                self._check_if_island_is_next_to_point(island, row, col)
                and island not in neighbors
            ):
                neighbors.append(island)

        return neighbors

    @staticmethod
    def _check_if_island_is_next_to_point(island: Island, row: int, col: int) -> bool:
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


def get_all_islands_next_to(col, line) -> int:
    try:
        if line[col] == "0":
            return col
    except IndexError:
        return col

    # mark field as visited
    line[col] = "#"

    return get_all_islands_next_to(col + 1, line)


def count_islands(path_to_file: str) -> int:
    island_counter = IslandCounter()
    for row, line in read_map_file(path_to_file):
        if all([item == "0" for item in line]):
            # if line cointains only 0 remove all island
            # we dont have to check previous islands when there are all 0 in line
            island_counter.remove_all_islands()
            continue

        num_cols = len(line)
        for col in range(num_cols):
            if line[col] == "#":
                continue

            if line[col] == "1":
                points = [
                    (row, col + point_nr)
                    for point_nr in range(get_all_islands_next_to(col, line) - col)
                ]
                island_counter.add_island(points)

    return island_counter.island_count

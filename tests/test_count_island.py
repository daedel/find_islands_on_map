import pytest
from src.map_reader.count_islands import (
    count_islands,
    IslandCounter,
    Island,
    get_all_islands_next_to,
)


@pytest.mark.parametrize(
    "input_file,island_count",
    [
        ("tests/resources/maps/map1.txt", 5),
        ("tests/resources/maps/map2.txt", 10),
        ("tests/resources/maps/map3.txt", 2),
    ],
)
def test_algorithm(input_file, island_count):
    islands = count_islands(input_file)
    assert islands == island_count


@pytest.mark.parametrize(
    "point,islands,neighbours_count",
    [
        ((2, 1), [Island([(1, 1), (1, 2)])], 1),
        ((2, 1), [Island([(1, 1), (1, 2)]), Island([(2, 3), (0, 1)])], 1),
        ((2, 1), [Island([(3, 4), (0, 1)])], 0),
        ((3, 4), [Island([(1, 3), (1, 4)])], 0),
        (
            (4, 5),
            [Island([(1, 1), (1, 2)]), Island([(4, 4)]), Island([(1, 1), (1, 2)])],
            1,
        ),
    ],
)
def test_get_neighbors_return_correct_number_of_islands(
    point, islands, neighbours_count
):
    island_counter = IslandCounter()
    [island_counter._insert_island(island) for island in islands]
    assert len(island_counter._get_neighbors(point[0], point[1])) == neighbours_count


@pytest.mark.parametrize(
    "points,islands",
    [
        ([(1, 3)], {Island([(1, 1), (1, 2)])}),
        ([(1, 3), (1, 4)], {Island([(1, 1), (1, 2)]), Island([(2, 3), (0, 1)])}),
        (
            [(1, 3), (1, 4), (1, 5)],
            {
                Island(
                    [(0, 2), (0, 3), Island([(2, 3), (0, 1)]), Island([(2, 3), (0, 1)])]
                )
            },
        ),
    ],
)
def test_merge_sub_islands_correct_count_of_islands(points, islands):
    island_counter = IslandCounter()
    [island_counter._insert_island(island) for island in islands]
    island_counter._merge_sub_islands(islands, points)
    assert island_counter.island_count == 1


@pytest.mark.parametrize(
    "point,island,expected_value",
    [
        ((2, 1), Island([(1, 1), (1, 2)]), True),
        ((3, 1), Island([(1, 1), (1, 2)]), False),
        ((0, 1), Island([(1, 1), (1, 2)]), True),
        ((6, 1), Island([(1, 1), (1, 2)]), False),
    ],
)
def test_check_islands_next_to_point(point, island, expected_value):
    assert (
        IslandCounter._check_if_island_is_next_to_point(island, point[0], point[1])
        == expected_value
    )


@pytest.mark.parametrize(
    "col,line,output",
    [
        (1, ["1", "0", "0"], 1),
        (2, ["1", "1", "0"], 2),
        (0, ["1", "1", "1"], 3),
        (0, ["1", "1", "0"], 2),
    ],
)
def test_get_all_islands_next_to(col, line, output):
    assert get_all_islands_next_to(col, line) == output

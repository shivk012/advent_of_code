import os
import unittest
from itertools import chain


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def process_data(data):
    """Convert the input into tuples of coordinates"""
    coords = []
    for line in data:
        start, end = line.split(" ->")
        start = start.split(",")
        end = end.split(",")
        start = (int(start[0]), int(start[1]))
        end = (int(end[0]), int(end[1]))
        coords.append((start, end))
    return coords


def find_horizontal_or_vertical(coords):
    """Return only the coordinates with x1=x2 or y1=y2"""
    return [
        line for line in coords if line[0][0] == line[1][0] or line[0][1] == line[1][1]
    ]


def get_max_coord(coords):
    """Get the maximum coordinate from the list of coordinates"""
    max_x = max(chain(*[x for x, y in coords]))
    max_y = max(chain(*[y for x, y in coords]))
    return max_x, max_y


def get_intersection_from_grid(grid, min_count):
    return len([x for x in chain(*grid) if x > min_count])


def map_vents(lines):
    """Map the vents into a list and return the list"""

    max_x, max_y = get_max_coord(lines)
    grid = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

    for line in lines:
        x_1 = line[0][0]
        x_2 = line[1][0]
        y_1 = line[0][1]
        y_2 = line[1][1]

        d_x = x_2 - x_1
        d_y = y_2 - y_1

        d_x = get_sign(d_x)
        d_y = get_sign(d_y)

        x, y = x_1, y_1

        while (x, y) != (x_2, y_2):
            grid[y][x] += 1
            x += d_x
            y += d_y

        grid[y_2][x_2] += 1

    return grid


def get_sign(d_x):
    if d_x < 0:
        d_x = -1
    elif d_x > 0:
        d_x = 1
    return d_x


def part_1(data):
    part_1_lines = find_horizontal_or_vertical(data)
    grid = map_vents(part_1_lines)

    return get_intersection_from_grid(grid, 1)


def part_2(data):
    grid = map_vents(data)

    return get_intersection_from_grid(grid, 1)


def main():
    data = read_data()
    data = process_data(data)
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """0,9 -> 5,9
                8,0 -> 0,8
                9,4 -> 3,4
                2,2 -> 2,1
                7,0 -> 7,4
                6,4 -> 2,0
                0,9 -> 2,9
                3,4 -> 1,4
                0,0 -> 8,8
                5,5 -> 8,2"""
    test_data = test_data.split("\n")
    test_data = process_data(test_data)

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 5)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 12)


if __name__ == "__main__":
    # unittest.main()
    main()

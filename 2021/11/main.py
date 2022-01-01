import os
import unittest
import numpy as np


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def create_grid(data):
    """Create a x,y grid of the data"""
    grid = np.zeros((len(data), len(data[0])), dtype=int)
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            grid[y, x] = char

    return grid


def get_flash(grid, flashed=[]):
    above_nine = np.where(grid > 9)
    flash_list = list(zip(above_nine[0], above_nine[1]))
    flash_list = [x for x in flash_list if x not in flashed]

    return set(flash_list)


def get_neighbours(grid, x, y):
    last_position = len(grid) - 1

    neighbour_coords = []
    if y > 0:
        neighbour_coords.append((x, y - 1))
    if y < last_position:
        neighbour_coords.append((x, y + 1))
    if x > 0:
        neighbour_coords.append((x - 1, y))
    if x < last_position:
        neighbour_coords.append((x + 1, y))
    if y > 0 and x > 0:
        neighbour_coords.append((x - 1, y - 1))
    if y > 0 and x < last_position:
        neighbour_coords.append((x + 1, y - 1))
    if y < last_position and x > 0:
        neighbour_coords.append((x - 1, y + 1))
    if y < last_position and x < last_position:
        neighbour_coords.append((x + 1, y + 1))
    return neighbour_coords


def part_1(data, steps=10, find_all=False):
    grid = create_grid(data)
    flashes = 0
    for step in range(steps):
        grid += 1
        already_flashed = set()
        to_flash = get_flash(grid, flashed=already_flashed)

        while to_flash:
            x, y = to_flash.pop()
            grid[x, y] = 0
            if sum(sum(grid)) == 0 and find_all:
                return step + 1
            already_flashed.add((x, y))
            neighbours = get_neighbours(grid, x, y)
            for nx, ny in neighbours:
                if (nx, ny) not in already_flashed:
                    grid[nx, ny] += 1
                    to_flash = set.union(
                        to_flash, get_flash(grid, flashed=already_flashed)
                    )
        flashes += len(already_flashed)
    return flashes


def part_2(data):
    return part_1(data, steps=1000, find_all=True)


def main():
    data = read_data()
    print(f"{part_1(data,steps=100)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """5483143223
                2745854711
                5264556173
                6141336146
                6357385478
                4167524645
                2176841721
                6882881134
                4846848554
                5283751526"""

    test_data = test_data.split("\n")
    test_data = [x.strip() for x in test_data]

    def test_1(self):
        self.assertEqual(part_1(self.test_data, 100), 1656)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 195)


if __name__ == "__main__":
    # unittest.main()
    main()

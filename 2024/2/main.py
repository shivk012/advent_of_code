import os
import unittest

import itertools


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def check_row_is_safe(row: list[int]) -> bool:
    pairs = itertools.pairwise(row)
    diffs = [b - a for b, a in pairs]

    if any(x < -3 for x in diffs) or any(x > 3 for x in diffs):
        return False

    if not all(x < 0 for x in diffs) and not all(x > 0 for x in diffs):
        return False

    return True


def part_1(data):
    safe = 0
    data = [[*map(int, report.split())] for report in data]
    for row in data:
        safe += check_row_is_safe(row)

    return safe


def part_2(data):
    safe = 0
    data = [[*map(int, report.split())] for report in data]
    for row in data:
        safe += check_row_is_safe(row) or any(
            check_row_is_safe(row[:index] + row[index + 1 :])
            for index in range(len(row))
        )

    return safe


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 2)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)


if __name__ == "__main__":
    # unittest.main()
    main()

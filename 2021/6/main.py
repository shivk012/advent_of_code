import os
import unittest
from collections import Counter


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def process_data(data):
    """Convert string seperated by comma into a list of integers"""
    data = data[0].split(",")
    data = list(map(lambda x: int(x), data))
    return data


def grow_fish(data, days: int):
    fish = Counter(data)
    for _ in range(days):
        (
            fish[0],
            fish[1],
            fish[2],
            fish[3],
            fish[4],
            fish[5],
            fish[6],
            fish[7],
            fish[8],
        ) = (
            fish[1],
            fish[2],
            fish[3],
            fish[4],
            fish[5],
            fish[6],
            fish[7] + fish[0],
            fish[8],
            fish[0],
        )
    return sum(fish.values())


def part_1(data):
    return grow_fish(data, 80)


def part_2(data):
    return grow_fish(data, 256)


def main():
    data = read_data()
    data = process_data(data)

    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """3,4,3,1,2"""
    test_data = test_data.split("\n")
    test_data = process_data(test_data)

    def test_1(self):
        self.assertEqual(grow_fish(self.test_data, 18), 26)

    def test_2(self):
        self.assertEqual(grow_fish(self.test_data, 80), 5934)


if __name__ == "__main__":
    # unittest.main()
    main()

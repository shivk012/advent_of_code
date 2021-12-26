import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def solver(data, steps):
    return sum([x < y for x, y in zip(data, data[steps:])])


def part_1(data):
    return solver(data, 1)


def part_2(data):
    return solver(data, 3)


def main():
    data = read_data()
    data = list(map(int, data))
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """199
                200
                208
                210
                200
                207
                240
                269
                260
                263"""
    test_data = test_data.split("\n")
    test_data = list(map(int, test_data))

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 7)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)


if __name__ == "__main__":
    # unittest.main()
    main()

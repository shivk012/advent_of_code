import os
import unittest
import statistics


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def process_data(data):
    data = data[0].split(",")
    data = list(map(lambda x: int(x), data))
    return data


def part_1(data):
    middle = statistics.median_low(data)
    return sum(map(lambda x: abs(x - middle), data))


def cost_part_2(step):
    """Cost for part two is n(n+1)/2"""
    return step * (step + 1) / 2


def part_2(data):
    # TODO: See if this can be derived rather than calculate all values
    # See: https://preview.redd.it/k4dnzf9it3481.png?width=1654&format=png&auto=webp&s=e3cc4c4af06ac8840dc521800d6f96032d87ea43
    cost = [
        sum(cost_part_2(abs(position - x)) for x in data)
        for position in range(0, max(data) + 1)
    ]

    return min(cost)


def main():
    data = read_data()
    data = process_data(data)
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """16,1,2,0,4,2,7,1,2,14"""
    test_data = test_data.split("\n")
    test_data = process_data(test_data)

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 37)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 168)


if __name__ == "__main__":
    # unittest.main()
    main()

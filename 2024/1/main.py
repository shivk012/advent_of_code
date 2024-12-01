import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.read()

    return data


def part_1(data):
    data = [*map(int, data.split())]
    a, b = sorted(data[0::2]), sorted(data[1::2])

    return sum(abs(x - y) for x, y in zip(a, b))


def part_2(data):
    data = [*map(int, data.split())]
    a, b = sorted(data[0::2]), sorted(data[1::2])

    return sum(x * b.count(x) for x in a)


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""
    test_data

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 11)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 2286)


if __name__ == "__main__":
    # unittest.main()
    main()

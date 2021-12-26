import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def move_sub(data):
    fwd, depth, aim, depth_2 = 0, 0, 0, 0

    for line in data:
        direction, value = line.split()
        value = int(value)

        if direction == "forward":
            fwd += value
            depth_2 += aim * value
        elif direction == "up":
            depth -= value
            aim -= value
        elif direction == "down":
            depth += value
            aim += value
        else:
            raise Exception(f"Unknown direction: {direction}")

    return fwd, depth, depth_2


def part_1(data):
    fwd, depth, _ = move_sub(data)
    return abs(fwd * depth)


def part_2(data):
    fwd, _, depth = move_sub(data)
    return abs(fwd * depth)


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """forward 5
                down 5
                forward 8
                up 3
                down 8
                forward 2"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 150)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 900)


if __name__ == "__main__":
    unittest.main()
    main()

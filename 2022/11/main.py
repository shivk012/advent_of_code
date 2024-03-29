import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data

def split_instructions(data):
    items = []
    operations = []
    tests = []
    throw_to = []

    for line in data:
        line = line.strip()
        match line.split(" "):
            case ["Starting",_, *line_items]:
                items.append([int(item.strip(",")) for item in line_items])
            case ["Operation:",_, _, first, operation, second]:
                operations.append((first, operation, second))
            case ["Test:", _, _, test]:
                tests.append(test)
            case ["If", "true:", "throw", "to", "monkey", to]:
                throw_to.append([0 , to])
            case ["If", "false:", "throw", "to", "monkey", to]:
                throw_to[-1][0] = to

    return items[::-1], operations[::-1], tests[::-1], throw_to[::-1]


def part_1(data):
    items, operations, tests, throw_to = split_instructions(data)
    for rnd in range(20):
        


def part_2(data):
    pass


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 10605)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)


if __name__ == "__main__":
    unittest.main()
    # main()

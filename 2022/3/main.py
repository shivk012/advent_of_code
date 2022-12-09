import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def get_priority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27


def part_1(data):

    priority_out = 0

    for rucksack in data:
        split = len(rucksack) // 2
        (repeated_item,) = set(rucksack[:split]) & set(rucksack[split:])
        priority_out += get_priority(repeated_item)

    return priority_out


def part_2(data):

    priority_out = 0
    for i in range(0, len(data), 3):
        repeated_item, = set(data[i]) & set(data[i + 1]) & set(data[i + 2])
        priority_out+= get_priority(repeated_item)
    return priority_out


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 157)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 70)


if __name__ == "__main__":
    # unittest.main()
    main()

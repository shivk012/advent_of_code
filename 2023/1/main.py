import os
import unittest
import re


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def part_1(data):
    sum_ = 0
    for line in data:
        matches = re.findall(r"\d", line)
        sum_ += int(matches[0] + matches[-1])
    return sum_


def part_2(data):
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    sum_ = 0
    for line in data:
        matches = re.findall(r"(?=(\d|"+"|".join(digit_map)+"))", line)
        matches = [digit_map.get(x, x) for x in matches]
        sum_ += int(matches[0] + matches[-1])

    return sum_

def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    test_data_1 = test_data_1.split("\n")

    test_data_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    test_data_2 = test_data_2.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data_1), 142)

    def test_2(self):
        self.assertEqual(part_2(self.test_data_2), 281)


if __name__ == "__main__":
    # unittest.main()
    main()

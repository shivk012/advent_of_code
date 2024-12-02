import re
import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.read()

    return data


def get_adjacent_numbers(data, location):
    output = []
    line_length = data.find("\n")
    line = data[
        location // line_length * line_length : location // line_length * line_length
        + line_length
    ]

    same_line = re.findall(r"(\d+)*\*(\d+)*", line)[0]
    output.extend(int(match) for match in same_line if match)

    above_line_left = data[(location - line_length)//line_length : location - line_length]
    above_line_right = data[location - line_length: location // line_length * line_length ]
    below_line_left = data[(location + line_length)//line_length*line_length + 2 : location + line_length + 2]
    below_line_right = data[location + line_length + 2 : (location + line_length)//line_length*line_length + line_length + 2]

    output.extend(
        int(match) for match in re.findall(r"(\d+)*\*(\d+)*", above_line_left) if match
    )
    output.extend(
        int(match) for match in re.findall(r"(\d+)*\*(\d+)*", above_line_right) if match
    )
    output.extend(
        int(match) for match in re.findall(r"(\d+)*\*(\d+)*", below_line_left) if match
    )
    output.extend(
        int(match) for match in re.findall(r"(\d+)*\*(\d+)*", below_line_right) if match
    )
    return output


def part_1(data):
    sum_ = 0
    for match in re.finditer(r"[^0-9.\na-z]", data, re.MULTILINE):
        get_adjacent_numbers(data, match.start())
    return sum_

def part_2(data):
    pass


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 7)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)


if __name__ == "__main__":
    unittest.main()
    # main()

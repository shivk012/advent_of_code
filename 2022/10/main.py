import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def calculate_x_values_per_cycle(data) -> list[int]:
    x_values = [1]
    for line in data:
        match line.split():
            case ["noop"]:
                x_values.append(x_values[-1])
            case ["addx", x]:
                x_values.append(x_values[-1])
                x_values.append(x_values[-1] + int(x))
    return x_values


def part_1(data):
    x_values = calculate_x_values_per_cycle(data)
    return (
        x_values[19] * 20
        + x_values[59] * 60
        + x_values[99] * 100
        + x_values[139] * 140
        + x_values[179] * 180
        + x_values[219] * 220
    )


def part_2(data):
    output = ""
    x_values = calculate_x_values_per_cycle(data)
    for i, sprite_location in enumerate(x_values[:]):
        cycle = i
        if not cycle % 40:
            output += "\n"
        if cycle % 40 in (sprite_location - 1, sprite_location, sprite_location + 1):
            output += "#"
        else:
            output += "."
    print()
    print()
    print(output)
    return output.strip()[:-2]


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 13140)

    def test_2(self):
        self.assertEqual(
            part_2(self.test_data),
            """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""",
        )


if __name__ == "__main__":
    # unittest.main()
    main()

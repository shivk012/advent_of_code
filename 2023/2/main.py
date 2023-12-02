
import os
import unittest
import re

def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, 'r') as f:
        data = f.readlines()
        
    data = list(map(lambda x: x.strip(), data))
    
    return data

def parse_line(line: str) -> tuple[int, int, int]:
    """Return the max number of red, blue and green in a line"""
    red = max((int(x) for x in re.findall(r'(\d+) red', line)), default=0)
    blue = max((int(x) for x in re.findall(r'(\d+) blue', line)), default=0)
    green = max((int(x) for x in re.findall(r'(\d+) green', line)), default=0)

    return (red, blue, green)
def part_1(data) -> int:
    output = 0
    for line in data:
        red, blue, green = parse_line(line)
        if not any([red > 12, blue > 14, green > 13]):
            game_id = int(re.findall(r'Game (\d+):', line)[0])
            output += game_id
    return output

def part_2(data) -> int:
    output = 0
    for line in data:
        red, blue, green = parse_line(line)
        power = max(red, 1) * max(blue, 1) * max(green, 1)
        output += power
    return output


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 8)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 2286)

if __name__ == "__main__":
    # unittest.main()
    main()


import os
import unittest

def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, 'r') as f:
        data = f.readlines()
        
    data = list(map(lambda x: x.strip(), data))
    
    return data


def part_1(data):
    cycles = [1]

    for instruction in data:
        print(f"cycles_count: {len(cycles)=}")
        print(instruction)
        match instruction.split(" "):
            case ["noop"]: 
                cycles.append(cycles[-1])
            case ["addx", x]:
                cycles.append(cycles[-1])
                cycles.append(cycles[-1] + int(x))
        print(cycles)
    output = 0
    for x in [20, 60, 100, 140, 180, 220]:
        print(f"{x=}: {cycles[x]=} {x*cycles[x]=}")
        output += x*cycles[x]
    return output
def part_2(data):
    pass


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = '''addx 15
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
noop'''

    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 13140)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)

if __name__ == "__main__":
    unittest.main()
    #main()

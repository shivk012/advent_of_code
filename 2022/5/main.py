import os
import unittest
from collections import deque


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def part_1(data):

    split_index = data.index("")
    stack_info = data[:split_index]
    instructions = data[split_index+1:]

    stacks_needed = int(stack_info[-1].strip().split(" ")[-1])

    stacks = {i+1:deque([]) for i in range(stacks_needed)}

    for line in stack_info[:-1]:
        for i, box in enumerate(line[1::4]):
            stacks[i+1].append(box) if box.strip() else None

    for line in instructions:
        _, number_of_boxes, _, from_stack, _, to_stack = line.split(" ")
        for _ in range(int(number_of_boxes)):
            stacks[int(to_stack)].appendleft(stacks[int(from_stack)].popleft())

    output = ''.join(f"[{' '.join(stack.popleft())}] " for stack in stacks.values())
    return output.replace("[", "").replace("]", "").replace(" ", "")
    
def part_2(data):
    split_index = data.index("")
    stack_info = data[:split_index]
    instructions = data[split_index+1:]

    stacks_needed = int(stack_info[-1].strip().split(" ")[-1])

    stacks = {i+1:deque([]) for i in range(stacks_needed)}

    for line in stack_info[:-1]:
        for i, box in enumerate(line[1::4]):
            stacks[i+1].append(box) if box.strip() else None

    for line in instructions:
        _, number_of_boxes, _, from_stack, _, to_stack = line.split(" ")
        for i in range(int(number_of_boxes)):
            stacks[int(to_stack)].insert(i, stacks[int(from_stack)].popleft())

    output = ''.join(f"[{' '.join(stack.popleft())}] " for stack in stacks.values())
    return output.replace("[", "").replace("]", "").replace(" ", "")


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), "CMZ")

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)


if __name__ == "__main__":
    # unittest.main()
    main()

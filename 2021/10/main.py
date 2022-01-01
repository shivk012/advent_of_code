import os
import unittest

POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
OPENER = {")": "(", "]": "[", "}": "{", ">": "<"}
POINTS_2 = {")": 1, "]": 2, "}": 3, ">": 4}
CLOSER = {"(": ")", "[": "]", "{": "}", "<": ">"}

def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def part_1(data):
    score = 0
    for line in data:
        stack = []
        for char in line:
            if char in "({[<":
                stack.append(char)
            elif stack.pop() != OPENER[char]:
                score += POINTS[char]
                break
    return score


def part_2(data):
    scores = []
    for line in data:
        stack = []
        score = 0
        for c in line:
            if c in CLOSER:
                stack.append(c)
            elif stack.pop() != OPENER[c]:
                break
        else:
            while len(stack) > 0:
                c = CLOSER[stack.pop()]
                score = score * 5 + POINTS_2[c]
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """[({(<(())[]>[[{[]{<()<>>
                [(()[<>])]({[<{<<[]>>(
                {([(<{}[<>[]}>{[]{[(<()>
                (((({<>}<{<{<>}{[]{[]{}
                [[<[([]))<([[{}[[()]]]
                [{[{({}]{}}([{[{{{}}([]
                {<[[]]>}<{[{[{[]{()[[[]
                [<(<(<(<{}))><([]([]()
                <{([([[(<>()){}]>(<<{{
                <{([{{}}[<[[[<>{}]]]>[]]"""
    test_data = test_data.split("\n")
    test_data = [x.strip() for x in test_data]

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 26397)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 288957)


if __name__ == "__main__":
    # unittest.main()
    main()

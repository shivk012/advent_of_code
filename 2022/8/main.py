import os
import pathlib
import unittest

utils_path = pathlib.Path(__file__).parent.parent.parent.as_posix()
import sys

sys.path.append(utils_path)
import utils


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def part_1(data):
    visible_trees = 0

    rows = [[int(x) for x in row.strip()] for row in data]
    matrix = utils.matrix.LinkedMatrix(rows)

    for row in matrix:
        for tree in row:
            if all(tree.value>other_tree for other_tree in tree.below):
                visible_trees += 1
                continue
            if all(tree.value>other_tree for other_tree in tree.above):
                visible_trees += 1
                continue
            if all(tree.value>other_tree for other_tree in tree.right_of):
                visible_trees += 1
                continue
            if all(tree.value>other_tree for other_tree in tree.left_of):
                visible_trees += 1
                continue
    return visible_trees


def part_2(data):
    def _score_in_line(tree_value, other_trees):
        score = 0
        for tree in other_trees:
            score += 1
            if tree_value <= tree:
                break
        return score
    
    max_score = 0

    rows = [[int(x) for x in row.strip()] for row in data]
    matrix = utils.matrix.LinkedMatrix(rows)

    for row in matrix:
        for tree in row:
            scenic_score = 1
            scenic_score *= _score_in_line(tree.value, tree.below)
            scenic_score *= _score_in_line(tree.value, tree.above[::-1])
            scenic_score *= _score_in_line(tree.value, tree.right_of)
            scenic_score *= _score_in_line(tree.value, tree.left_of[::-1])
            if scenic_score > max_score:
                max_score = scenic_score
    return max_score

def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """30373
25512
65332
33549
35390"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 21)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 8)


if __name__ == "__main__":
    # unittest.main()
    main()

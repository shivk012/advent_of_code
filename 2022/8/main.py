import os
import unittest


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
    columns = list(zip(*rows))

    for i in range(len(rows)):
        for j in range(len(rows)):
            tree = rows[i][j]
            if (
                all(x < tree for x in rows[i][:j])
                or all(x < tree for x in rows[i][j + 1 :])
                or all(x < tree for x in columns[j][:i])
                or all(x < tree for x in columns[j][i + 1 :])
            ):
                visible_trees += 1

    return visible_trees

def part_2(data):
    pass


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
        self.assertEqual(part_2(self.test_data), 5)


if __name__ == "__main__":
    # unittest.main()
    main()

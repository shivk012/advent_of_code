import os
import unittest
from collections import defaultdict


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def create_graph(data):
    adjacency = defaultdict(list)
    for line in data:
        a, b = line.split("-")
        adjacency[a].append(b)
        adjacency[b].append(a)

    return adjacency


def part_1(data):
    graph = create_graph(data)
    visited = set()
    
    def paths(current, visited):
        if current == 'end':
            return 1
        if current in visited and current.islower():
            return 0
        visited = visited.union(set([current]))
        count = 0
        for cave in graph[current]:
            count += paths(cave, visited)
        return count

    return paths('start', visited)


def part_2(data):
    pass


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 10)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)


if __name__ == "__main__":
    unittest.main()
    # main()

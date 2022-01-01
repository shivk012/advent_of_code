import os
from typing import Tuple
import unittest
import networkx as nx
from math import prod


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def create_graph(data):
    height_map = nx.Graph()
    for y, line in enumerate(data):
        for x, value in enumerate(line):
            height_map.add_node((x, y), value=int(value))
            if x:
                height_map.add_edge((x, y), (x - 1, y))
            if y:
                height_map.add_edge((x, y), (x, y - 1))

    return height_map


def retun_neighbour_values(height_map, node: Tuple[int, int]):
    neighbours = height_map.neighbors(node)
    return [height_map.nodes[n]["value"] for n in neighbours]


def part_1(data):
    height_map = create_graph(data)
    lowest_vals = [
        height_map.nodes[location]["value"] + 1
        for location in height_map.nodes
        if height_map.nodes[location]["value"]
        < min(retun_neighbour_values(height_map, location))
    ]

    return sum(lowest_vals)


def part_2(data):
    height_map = create_graph(data)
    for x, y in height_map.nodes:
        if height_map.nodes[(x, y)]["value"] == 9:
            height_map.remove_edges_from(
                [((x, y), node) for node in height_map.neighbors((x, y))]
            )

    top_three_basins = sorted(
        nx.connected_components(height_map), key=len, reverse=True
    )[:3]

    return prod(len(basin) for basin in top_three_basins)


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """2199943210
                    3987894921
                    9856789892
                    8767896789
                    9899965678"""
    test_data = test_data.split("\n")
    test_data = [x.strip() for x in test_data]

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 15)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 1134)


if __name__ == "__main__":
    # unittest.main()
    main()

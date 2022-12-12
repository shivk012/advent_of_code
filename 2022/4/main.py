
import os
import unittest

def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, 'r') as f:
        data = f.readlines()
        
    data = list(map(lambda x: x.strip(), data))
    
    return data


def _contained_by_range(range1:tuple[int,int], range2:tuple[int,int])->bool:
    """Range 1 fully contains Range 2 if (x1 <= x2) and (y1 >= y2)"""
    x1, y1 = range1
    x2, y2 = range2
    return (x1 <= x2) and (y1 >= y2)

def _overlapping_ranges(range1:tuple[int,int], range2:tuple[int,int])->bool:
    """Range 1 and Range 2 overlap if (x1 <= y2) and (y1 >= x2)"""
    x1, y1 = range1
    x2, y2 = range2
    return (x1 <= y2) and (y1 >= x2)

def part_1(data):
    """Range 1 fully contains Range 2 if (x1 <= x2) and (y1 >= y2)"""
    pairs = 0
    for assignment in data:
        range1, range2 = assignment.split(",")
        range1 = tuple(map(int, range1.split("-")))
        range2 = tuple(map(int, range2.split("-")))
        
        # check if range1 contains range2
        if _contained_by_range(range1, range2) or _contained_by_range(range2, range1):
            pairs += 1
    return pairs

def part_2(data):
    pairs = 0
    for assignment in data:
        range1, range2 = assignment.split(",")
        range1 = tuple(map(int, range1.split("-")))
        range2 = tuple(map(int, range2.split("-")))
        
        # check if range1 contains range2
        if _overlapping_ranges(range1, range2) or _overlapping_ranges(range2, range1):
            pairs += 1
    return pairs


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 2)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 4)

if __name__ == "__main__":
    # unittest.main()
    main()


import os
import unittest
from collections import defaultdict
from itertools import accumulate

def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, 'r') as f:
        data = f.readlines()
        
    data = list(map(lambda x: x.strip(), data))
    
    return data


def part_1(data):
    sizes = defaultdict(int)
    current_dir = ['/']
    
    for line in data:
        print(line)
        match line.split():
            case '$', 'cd', '/': 
                current_dir = ['/']
            case '$', 'cd', '..': 
                current_dir.pop()
            case '$', 'cd', x: 
                current_dir.append(f'{x}/')
            case '$', 'ls': 
                pass
            case 'dir', _: 
                pass
            case size, _:
                for p in accumulate(current_dir):
                    print(p)
                    print(current_dir)
                    sizes[p] += int(size)
            case _: 
                pass

    return sum(file_size for file_size in sizes.values() if file_size < 100_000)

def part_2(data):
    sizes = defaultdict(int)
    current_dir = ['/']
    
    for line in data:
        print(line)
        match line.split():
            case '$', 'cd', '/': 
                current_dir = ['/']
            case '$', 'cd', '..': 
                current_dir.pop()
            case '$', 'cd', x: 
                current_dir.append(f'{x}/')
            case '$', 'ls': 
                pass
            case 'dir', _: 
                pass
            case size, _:
                for p in accumulate(current_dir):
                    print(p)
                    print(current_dir)
                    sizes[p] += int(size)
            case _: 
                pass

    required_free_space = 30_000_000
    current_free_space = 70_000_000 - max(sizes.values())

    return min(file_size for file_size in sizes.values() if file_size > required_free_space - current_free_space)
    
def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 95437)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 5)

if __name__ == "__main__":
    # unittest.main()
    main()

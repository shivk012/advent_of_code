
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
    # treat grid as a complex plane
    head = 0+0j
    tail = 0+0j
    directional_movement = {'R':+1, 'L':-1, 'U':1j, 'D':-1j}
    seen = {tail}
    tail_movement = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))
    
    for line in data:
        direction = line[0]
        steps = int(line[2:])

        for i in range(steps):
            head += directional_movement[direction]
            # needs to be 2 so that a diagonal separation doesn't count as 1
            if abs(head-tail) >=2 :
                tail += tail_movement(head-tail)
                seen.add(tail)
    return len(seen)

def part_2(data):
    rope = [0+0j] * 10
    directional_movement = {'R':+1, 'L':-1, 'U':1j, 'D':-1j}
    seen = [set([x]) for x in rope]
    tail_movement = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))
    
    for line in data:
        direction = line[0]
        steps = int(line[2:])

        for _ in range(steps):
            rope[0] += directional_movement[direction]
            # needs to be 2 so that a diagonal separation doesn't count as 1
            for i in range(1,10):
                dist = rope[i-1]-rope[i]
                if abs(dist) >=2 :
                    rope[i] += tail_movement(dist)
                    seen[i].add(rope[i])

    return len(seen[9])


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

    test_data_2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

    test_data = test_data.split("\n")
    test_data_2 = test_data_2.split("\n")
    
    def test_1(self):
        self.assertEqual(part_1(self.test_data), 13)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 1)

    def test_3(self):
        self.assertEqual(part_2(self.test_data_2), 36)
if __name__ == "__main__":
    # unittest.main()
    main()

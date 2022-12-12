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
    data = data[0]
    for window_start, window_end in enumerate(range(4, len(data))):
        window = data[window_start:window_end]

        if len(set(window)) == len(window):
            return window_end


def part_2(data):
    data = data[0]
    for window_start, window_end in enumerate(range(14, len(data))):
        window = data[window_start:window_end]

        if len(set(window)) == len(window):
            return window_end


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    test_data_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    test_data_3 = "nppdvjthqldpwncqszvftbrmjlhg"
    test_data_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    test_data_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    def test_1_1(self):
        self.assertEqual(part_1(self.test_data_1), 7)
    def test_1_2(self):
        self.assertEqual(part_1(self.test_data_2), 5)
    def test_1_3(self):
        self.assertEqual(part_1(self.test_data_3), 6)
    def test_1_4(self):
        self.assertEqual(part_1(self.test_data_4), 10)
    def test_1_5(self):
        self.assertEqual(part_1(self.test_data_5), 11)

    def test_2_1(self):
        self.assertEqual(part_1(self.test_data_1), 19)
    def test_2_2(self):
        self.assertEqual(part_1(self.test_data_2), 23)
    def test_2_3(self):
        self.assertEqual(part_1(self.test_data_3), 23)
    def test_2_4(self):
        self.assertEqual(part_1(self.test_data_4), 29)
    def test_2_5(self):
        self.assertEqual(part_1(self.test_data_5), 26)


if __name__ == "__main__":
    # unittest.main()
    main()

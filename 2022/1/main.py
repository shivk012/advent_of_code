import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def get_total_calories_by_elf(data):
    output = [0] * (data.count("") + 1)
    output_index = 0

    for food in data:
        if not food:
            output_index += 1
            continue

        output[output_index] += int(food)
    return output


def part_1(data):
    output = get_total_calories_by_elf(data)

    max_calories = max(output)
    index_of_max_calories = output.index(max_calories)

    return index_of_max_calories + 1, max_calories


def part_2(data):
    output = get_total_calories_by_elf(data)
    output.sort(reverse=True)
    return sum(output[:3])


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), (4, 24000))

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 45000)


if __name__ == "__main__":
    # unittest.main()
    main()


import os
import sys

def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, 'r') as f:
        data = f.readlines()
        
    data = list(map(lambda x: x.strip(), data))
    
    return data

def part_1():
    pass


def part_2():
    pass


def main():
    data = read_data()
    print(f"{part_1()=}")
    print(f"{part_2()=}")

if __name__ == "__main__":
    main()

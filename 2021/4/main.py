import os
from typing import List, Tuple, Union
import unittest
import numpy as np


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def process_data(data) -> Tuple[List[int], List]:
    """Take the instructions and split the number draws from the boards. Boards are converted into a numpy array"""
    draw = data[0].split(",")
    draw = [int(x) for x in draw]

    board_in = data[2:]
    board_out = []

    for board_start in range(0, len(board_in), 6):
        board = board_in[board_start : board_start + 5]
        board = [x.split() for x in board]
        board = np.array(board, dtype=int)
        board_out.append(board)
    return draw, board_out


def play_turn(number: int, boards: List[np.ndarray]) -> List[np.ndarray]:
    """Play one turn of bingo. Works by marking the called out number as -1 in all the boards"""
    for board in boards:
        board[np.where(board == number)] = -1
    return boards


def check_win(boards: List[np.ndarray]) -> Union[List, List]:
    """Check if the board has any rows or columns with all -1s"""
    won = []
    ongoing = []
    for board in boards:
        called = board == -1
        if called.all(axis=0).any() or called.all(axis=1).any():
            won.append(board)
        else:
            ongoing.append(board)
    return won, ongoing


def play_bingo(data) -> Tuple[int, np.ndarray, int, np.ndarray]:
    """Play the game by calling out numbers and checking for wins"""
    draw, boards = data
    boards_finished = 0
    total_boards = len(boards)

    for number in draw:
        boards = play_turn(number, boards)
        win, boards = check_win(boards)

        if win:
            if not boards_finished:
                first_board = win[0]
                first_number = number

            boards_finished = total_boards - len(boards)
            if boards_finished == total_boards:
                last_board = win[0]
                break

    return first_number, first_board, number, last_board


def calculate_score(number, winning_board):
    return number * winning_board[winning_board > -1].sum()


def part_1(data):
    number, winning_board, _, _ = data
    return calculate_score(number, winning_board)


def part_2(data):
    _, _, number, winning_board = data
    return calculate_score(number, winning_board)


def main():
    data = read_data()
    data = process_data(data)
    winning_outputs = play_bingo(data)
    print(f"{part_1(winning_outputs)=}")
    print(f"{part_2(winning_outputs)=}")


class Test(unittest.TestCase):
    test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

                22 13 17 11  0
                8  2 23  4 24
                21  9 14 16  7
                6 10  3 18  5
                1 12 20 15 19

                3 15  0  2 22
                9 18 13 17  5
                19  8  7 25 23
                20 11 10 24  4
                14 21 16 12  6

                14 21 17 24  4
                10 16 15  9 19
                18  8 23 26 20
                22 11 13  6  5
                2  0 12  3  7"""
    test_data = test_data.split("\n")
    test_data = process_data(test_data)

    def test_01_process_data(self):
        draw = [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ]
        board = [
            np.array(
                [
                    [22, 13, 17, 11, 0],
                    [8, 2, 23, 4, 24],
                    [21, 9, 14, 16, 7],
                    [6, 10, 3, 18, 5],
                    [1, 12, 20, 15, 19],
                ]
            ),
            np.array(
                [
                    [3, 15, 0, 2, 22],
                    [9, 18, 13, 17, 5],
                    [19, 8, 7, 25, 23],
                    [20, 11, 10, 24, 4],
                    [14, 21, 16, 12, 6],
                ]
            ),
            np.array(
                [
                    [14, 21, 17, 24, 4],
                    [10, 16, 15, 9, 19],
                    [18, 8, 23, 26, 20],
                    [22, 11, 13, 6, 5],
                    [2, 0, 12, 3, 7],
                ]
            ),
        ]
        self.assertEqual(draw, self.test_data[0])
        np.testing.assert_array_equal(board, self.test_data[1])

    def test_02_part_1(self):
        self.assertEqual(part_1(self.test_data), 4512)

    def test_03_part_2(self):
        self.assertEqual(part_2(self.test_data), 1924)


if __name__ == "__main__":
    # unittest.main()
    main()

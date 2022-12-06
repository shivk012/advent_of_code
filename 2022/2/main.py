import os
import unittest


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def solution_1(data):
    """The brute solution"""
    score = 0
    score_lookup = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]

    for play in data:
        if not play:
            continue

        play = play.replace(" ", "")
        score += score_lookup.index(play) + 1

    return score


def part_1(data):
    """A for Rock, B for Paper, C for Scissors
    X for Rock, Y for Paper, Z for Scissors

    Score
    X = 1
    Y = 2
    Z = 3

    Loss = 0
    Draw = 3
    Win = 6

    AX = 4
    AY = 8
    AZ = 3

    BX = 1
    BY = 5
    BZ = 9

    CX = 7
    CY = 2
    CZ = 6
    """
    RESULT_SCORES = {"LOSS": 0, "DRAW": 3, "WIN": 6}
    PLAY_LOOKUP = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for play in data:
        play = play.replace(" ", "")
        if not play:
            continue

        match list(play):
            case ["A", chosen]:
                # Opponent chose Rock
                match chosen:
                    case "X":
                        score += RESULT_SCORES["DRAW"]
                    case "Y":
                        score += RESULT_SCORES["WIN"]
                    case "Z":
                        score += RESULT_SCORES["LOSS"]
                score += PLAY_LOOKUP[chosen]
            case ["B", chosen]:
                # Opponent chose Paper
                match chosen:
                    case "X":
                        score += RESULT_SCORES["LOSS"]
                    case "Y":
                        score += RESULT_SCORES["DRAW"]
                    case "Z":
                        score += RESULT_SCORES["WIN"]
                score += PLAY_LOOKUP[chosen]
            case ["C", chosen]:
                # Opponent chose Scissors
                match chosen:
                    case "X":
                        score += RESULT_SCORES["WIN"]
                    case "Y":
                        score += RESULT_SCORES["LOSS"]
                    case "Z":
                        score += RESULT_SCORES["DRAW"]
                score += PLAY_LOOKUP[chosen]
    return score


def part_2(data):
    RESULT_SCORES = {"LOSS": 0, "DRAW": 3, "WIN": 6}
    PLAY_LOOKUP = {"Rock": 1, "Paper": 2, "Scissors": 3}
    score = 0
    for play in data:
        play = play.replace(" ", "")
        if not play:
            continue

        match list(play):
            case ["A", outcome]:
                # Opponent chose Rock
                match outcome:
                    case "X":
                        score += RESULT_SCORES["LOSS"]
                        chosen = "Scissors"
                    case "Y":
                        score += RESULT_SCORES["DRAW"]
                        chosen = "Rock"
                    case "Z":
                        score += RESULT_SCORES["WIN"]
                        chosen = "Paper"
                score += PLAY_LOOKUP[chosen]
            case ["B", outcome]:
                # Opponent chose Paper
                match outcome:
                    case "X":
                        score += RESULT_SCORES["LOSS"]
                        chosen = "Rock"
                    case "Y":
                        score += RESULT_SCORES["DRAW"]
                        chosen = "Paper"
                    case "Z":
                        score += RESULT_SCORES["WIN"]
                        chosen = "Scissors"
                score += PLAY_LOOKUP[chosen]
            case ["C", outcome]:
                # Opponent chose Scissors
                match outcome:
                    case "X":
                        score += RESULT_SCORES["LOSS"]
                        chosen = "Paper"
                    case "Y":
                        score += RESULT_SCORES["DRAW"]
                        chosen = "Scissors"
                    case "Z":
                        score += RESULT_SCORES["WIN"]
                        chosen = "Rock"
                score += PLAY_LOOKUP[chosen]
    return score


def test(data):
    class Choice:
        WIN_CONDITION = None
        LOSS_CONDITION = None

        def get_result(self, opponent):
            if opponent == self.LOSS_CONDITION:
                return "WIN"
            elif opponent == self.WIN_CONDITION:
                return "LOSS"
            else:
                return "DRAW"

        def get_required_move(self, result) -> str:
            if result == "WIN":
                return self.LOSS_CONDITION
            elif result == "LOSS":
                return self.WIN_CONDITION
            else:
                return self.__class__.__name__

        def __repr__(self) -> str:
            return self.__class__.__name__
    class Rock(Choice):
        WIN_CONDITION = "Scissors"
        LOSS_CONDITION = "Paper"

    class Paper(Choice):
        WIN_CONDITION = "Rock"
        LOSS_CONDITION = "Scissors"

    class Scissors(Choice):
        WIN_CONDITION = "Paper"
        LOSS_CONDITION = "Rock"

    RESULT_SCORES = {"LOSS": 0, "DRAW": 3, "WIN": 6}
    PLAY_LOOKUP = {"Rock": 1, "Paper": 2, "Scissors": 3}
    OPPONENT_LOOKUP = {"A": Rock, "B": Paper, "C": Scissors}
    PART_1_LOOKUP = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
    PART_2_LOOKUP = {"X": "LOSS", "Y": "DRAW", "Z": "WIN"}

    score_part_1 = 0
    score_part_2 = 0

    for play in data:
        play = play.replace(" ", "")
        if not play:
            continue

        opponent_play = OPPONENT_LOOKUP[play[0]]()

        part_1_result = opponent_play.get_result(PART_1_LOOKUP[play[1]])
        score_part_1 += RESULT_SCORES[part_1_result]
        score_part_1 += PLAY_LOOKUP[opponent_play.get_required_move(part_1_result)]

        part_2_result = opponent_play.get_required_move(PART_2_LOOKUP[play[1]])
        score_part_2 += RESULT_SCORES[PART_2_LOOKUP[play[1]]]
        score_part_2 += PLAY_LOOKUP[part_2_result]

    return score_part_1, score_part_2

def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")
    print(f"{test(data)=}")

class Test(unittest.TestCase):
    test_data = """A Y
B X
C Z"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 15)
        self.assertEqual(test(self.test_data)[0], 15)
    def test_2(self):
        self.assertEqual(part_2(self.test_data), 12)
        self.assertEqual(test(self.test_data)[1], 12)


if __name__ == "__main__":
    # unittest.main()
    main()

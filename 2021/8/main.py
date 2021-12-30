import os
import unittest
from collections import Counter

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def get_digit(output_value):
    l = len(output_value)
    if l == 2:
        return 1
    elif l == 3:
        return 7
    elif l == 4:
        return 4
    elif l == 7:
        return 8
    else:
        return 0


def part_1(data):
    all_digits = " ".join([line.split("|")[1].strip() for line in data]).strip()
    all_digits_count = Counter(get_digit(x) for x in all_digits.split())

    return (
        all_digits_count[1]
        + all_digits_count[4]
        + all_digits_count[7]
        + all_digits_count[8]
    )


def figure_out_digits(signal):
    one_signal = [sig for sig in signal if len(sig) == 2][0]
    seven_signal = [sig for sig in signal if len(sig) == 3][0]
    four_signal = [sig for sig in signal if len(sig) == 4][0]
    eight_signal = [sig for sig in signal if len(sig) == 7][0]

    # len is 5 can be 2,3,5
    five_len = [sig for sig in signal if len(sig) == 5]
    three_signal = [sig for sig in five_len if set(seven_signal).issubset(sig)][0]
    five_signal = [
        sig
        for sig in five_len
        if len(set(four_signal).intersection(sig)) == 3
        and len(set(one_signal).intersection(sig)) == 1
    ][0]
    two_signal = [sig for sig in five_len if sig not in [three_signal, five_signal]][0]

    # len is 6 can be 0,6,9
    six_len = [sig for sig in signal if len(sig) == 6]
    nine_signal = [sig for sig in six_len if set(four_signal).issubset(sig)][0]
    zero_signal = [
        sig
        for sig in six_len
        if sig not in [nine_signal] and set(seven_signal).issubset(sig)
    ][0]
    six_signal = [sig for sig in six_len if sig not in [zero_signal, nine_signal]][0]

    return {
        one_signal: "1",
        two_signal: "2",
        three_signal: "3",
        four_signal: "4",
        five_signal: "5",
        six_signal: "6",
        seven_signal: "7",
        eight_signal: "8",
        nine_signal: "9",
        zero_signal: "0",
    }


def part_2(data):
    total = 0
    for line in data:
        signal, value = line.split("|")
        signal = sorted(signal.strip().split(" "), key=len)
        signal = ["".join(sorted(sig)) for sig in signal]
        digits = figure_out_digits(signal)

        value = value.strip().split(" ")
        out_val = int("".join([digits["".join(sorted(val))] for val in value]))
        total += out_val

    return total


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


class Test(unittest.TestCase):
    test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
                edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
                fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
                fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
                aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
                fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
                dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
                bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
                egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
                gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    test_data = test_data.split("\n")

    def test_1(self):
        self.assertEqual(part_1(self.test_data), 26)

    def test_2(self):
        self.assertEqual(part_2(self.test_data), 61229)


if __name__ == "__main__":
    # unittest.main()
    main()

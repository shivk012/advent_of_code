from collections import Counter
import os
import re


def read_data():
    dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(dir, "input.txt")

    with open(input_file, "r") as f:
        data = f.readlines()

    data = list(map(lambda x: x.strip(), data))

    return data


def read_bits(data):
    if not data:
        return "", ""

    data = [x.strip() for x in data]

    theta = ""
    epsilon = ""

    for i in range(len(data[0])):
        all_bits = "".join([rate[i] for rate in data])
        counts = Counter(all_bits)
        theta += counts["1"] >= counts["0"] and "1" or "0"
        epsilon += counts["1"] >= counts["0"] and "0" or "1"

    return theta, epsilon


def part_1(data):
    t, e = read_bits(data)
    return int(t, 2) * int(e, 2)


def part_2(data):
    t, e = read_bits(data)

    search_t = ""
    search_e = ""
    full_str_t = " " + " ".join(data) + " "
    full_str_e = " " + " ".join(data) + " "

    for i in range(len(t)):
        if t:
            search_t += t[i]
        if e:
            search_e += e[i]

        left_over_t = len(t) - i - 1
        left_over_e = len(e) - i - 1

        o_find = re.findall(
            r"\s" + search_t[0 : i + 1] + r".{" + str(left_over_t) + r"}", full_str_t
        )
        c_find = re.findall(
            r"\s" + search_e[0 : i + 1] + r".{" + str(left_over_e) + r"}", full_str_e
        )

        t, _ = read_bits(o_find)
        _, e = read_bits(c_find)

        full_str_t = " " + " ".join(o_find) + " "
        full_str_e = " " + " ".join(c_find) + " "

        if len(o_find) == 1:
            o = o_find[0]
        if len(c_find) == 1:
            c = c_find[0]

    return int(o, 2) * int(c, 2)


def main():
    data = read_data()
    print(f"{part_1(data)=}")
    print(f"{part_2(data)=}")


if __name__ == "__main__":
    main()

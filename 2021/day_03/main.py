#!/usr/bin/env python3

def remove_values(arr, indexes):
    indexes.sort()
    indexes.reverse()
    for index in indexes:
        arr.pop(index)

def get_rating(report, pref):
    index = 0
    while len(report) > 1:
        s = [0,0]
        indexes = [[],[]]

        count = 0
        for binary in report:
            bit = int(binary[index])

            s[bit] += 1
            indexes[bit].append(count)

            count += 1

        if s[0] > s[1]:
            remove_values(report, indexes[pref])
        else:
            remove_values(report, indexes[pref^1])

        index += 1

    return int(report.pop(), 2)

def part1(report):
    bits = ""
    bit_size = len(report[0])
    for i in range(bit_size):
        b = [0,0]

        for binary in report:
            b[int(binary[i])] += 1

        bits += "0" if b[0] > b[1] else "1"

    gamma = int(bits, 2)
    epsilon = ~gamma & 2**bit_size-1

    return gamma * epsilon

def part2(report):
    oxygen_report = report.copy()
    co2_report = report.copy()

    oxygen_rating = get_rating(oxygen_report, 1)
    co2_rating = get_rating(co2_report, 0)

    return oxygen_rating * co2_rating

if __name__ == "__main__":
    with open("input.txt") as f:
        report = [binary for binary in f.read().splitlines()]

    print(part1(report))
    print(part2(report))


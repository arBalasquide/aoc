#!/usr/bin/env python3

def part1(depths):
    ans = 0
    prev = float('inf')
    for depth in depths:
        if depth > prev:
            ans +=1

        prev = depth

    print(ans)

def part2(depths):
    ans = 0
    prev = depths[0] + depths[1] + depths[2]
    for i in range(1, len(depths)-1):
        depth = depths[i-1] + depths[i] + depths[i+1]

        if depth > prev:
            ans += 1

        prev = depth

    print(ans)

if __name__ == "__main__":
    with open("input.txt") as f:
        depths = [int(x) for x in f.read().splitlines()]

    part1(depths)
    part2(depths)

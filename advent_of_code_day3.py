# Advent of Code 2021 Day 3

with open("./data/input-day3.txt") as f:
    binary_nums = []

    for line in f:
        binary_nums.append(int(line))

    for i in range(len(binary_nums)):
        if (binary_nums[i])[0] == 1:
            pass
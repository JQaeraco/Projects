# Advent of Code 2021 Day 2

with open("./data/input-day2.txt") as f:
    directions = []

    for line in f:
        directions.append(str(line))

    position = 0
    horizontal_pos = 0
    depth = 0
    length = len(directions)
    no_newline_direction = []

    for i in directions:
        no_newline_direction.append(i.replace("\n", ""))

    for i in range(length):
        if (no_newline_direction[i])[0] == "u":
            depth -= int((no_newline_direction[i])[-1])
        elif (no_newline_direction[i])[0] == "d":
            depth += int((no_newline_direction[i])[-1])
        elif (no_newline_direction[i])[0] == "f":
            horizontal_pos += int((no_newline_direction[i])[-1])
        print(f"horizontal position: {horizontal_pos}\n depth: {depth}")

print(1957 * 955)
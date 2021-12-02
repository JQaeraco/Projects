# Advent of Code 2021 Day 1


# To open up the file
with open("./data/input-day1.txt") as f:
    depths = []

    # For every line in the file
    for line in f:
        # Add the INTEGER to a list of depths
        depths.append(int(line))

    length = len(depths)

    for i in range(length):
        if depths[i] == depths[0]:
            print("N/A - no previous measurement")
        elif depths[i] > depths[i-1]:
            print(f"{depths[i]} (increased)")
        elif depths[i] == depths[i-1]:
            print(f"{depths[i]} (no change)")
        else:
            print(f"{depths[i]} (decreased)")
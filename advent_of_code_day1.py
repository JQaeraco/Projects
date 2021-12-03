# Advent of Code 2021 Day 1


# To open up the file
# PART 1
# with open("./data/input-day1.txt") as f:
#     depths = []
#
#     # For every line in the file
#     for line in f:
#         # Add the INTEGER to a list of depths
#         depths.append(int(line))
#
#     length = len(depths)
#     num_of_increases = 0
#
#     for i in range(length):
#         if depths[i] == depths[0]:
#             print("N/A - no previous measurement")
#         elif depths[i] > depths[i-1]:
#             num_of_increases += 1
#             print(f"{depths[i]} (increased)")
#         elif depths[i] == depths[i-1]:
#             print(f"{depths[i]} (no change)")
#         else:
#             print(f"{depths[i]} (decreased)")
#
# print(num_of_increases)

# PART 2
with open("./data/input-day1.txt") as f:
    depths = []

    # For every line in the file
    for line in f:
        # Add the INTEGER to a list of depths
        depths.append(int(line))

    length = len(depths)
    num_of_increases = 0

    for i in range(length):
        if depths[i] == depths[0]:
            print("N/A - no previous measurement")
        elif depths[i] > depths[i-1]:
            num_of_increases += 1
            print(f"{depths[i]} (increased)")
        elif depths[i] == depths[i-1]:
            print(f"{depths[i]} (no change)")
        else:
            print(f"{depths[i]} (decreased)")

print(num_of_increases)
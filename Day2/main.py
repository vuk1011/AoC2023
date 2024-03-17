# Imports
import utils as ut


"""
Solution Part 1
"""

input_1 = ut.get_input("real_input.txt")

for i, row in enumerate(input_1):
    for j in range(1, len(row)):
        input_1[i][j] = ut.get_turn(input_1[i][j])

ids = []
for game in input_1:
    add = True
    for i in range(1, len(game)):
        if not ut.turn_is_possible(game[i]):
            add = False
    if add:
        ids.append(game[0])
print("Solution 1:", sum(ids))

"""
Solution Part 2
"""


input_2 = input_1[::]

min_sets = []
for game in input_2:
    min_set = {"red":   max([game[i]["red"] for i in range(1, len(game)) ]),
               "green": max([game[i]["green"] for i in range(1, len(game)) ]),
               "blue":  max([game[i]["blue"] for i in range(1, len(game)) ])}
    min_sets.append(min_set)

sol_2 = sum([ut.power_of_set(x) for x in min_sets])
print("Solution 2:", sol_2)
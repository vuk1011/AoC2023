from utils import *


"""
Part 1
"""

cards = get_data('input/input.txt')
solution1 = 0

for card in cards:
    winning = set(card[0])
    player = set(card[1])
    matches = len(winning.intersection(player))
    if matches > 0:
        solution1 += 2 ** (matches - 1)

print('Solution 1:', solution1)

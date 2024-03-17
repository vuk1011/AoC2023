from utils import *


"""
Part 1
"""

data = get_data('input/input.txt')
matrix = Matrix(data)
numbers = [Number(x) for x in matrix.get_numbers()]
solution1 = 0

for n in numbers:
    ngh = set()
    for pos in n.pos:
        ngh = ngh.union(matrix.get_neighbours_pos(pos))
    if neighbourhood_has_symbol(matrix, ngh):
        solution1 += n.val

print('Solution 1:', solution1)

"""
Part 2
"""

solution2 = 0

for row in matrix.elements:
    for el in row:
        if el.val == '*':
            ngh = matrix.get_neighbours_pos(el.pos)     # neighbouring positions to the *
            ngh_nums: list[Number] = []
            for num in numbers:     # get numbers in its neighbourhood
                if num.pos.intersection(ngh):
                    ngh_nums.append(num)
            if len(ngh_nums) == 2:
                solution2 += ngh_nums[0].val * ngh_nums[1].val

print('Solution 2:', solution2)

# Imports
import utils as ut


"""
Solution Part 1
"""

input_1 = ut.get_input("real_input.txt")

nums1 = [ut.get_num_1(line) for line in input_1]
sol1 = sum(nums1)
print("Solution 1:", sol1)


"""
Solution Part 2
"""

input_2 = ut.get_input("real_input.txt")

#nums_2 = [ut.get_num_2(line) for line in input_2]
#sol_2 = sum(nums_2)
#print("Solution 2:", sol_2)

print(ut.get_last_digit_index("u886a9"))

#!/usr/bin/env python3

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()
    
# Trim each line
values=[value.strip() for value in values]

# Shared helper
def countTrees(inc_x, inc_y):
    count=0
    x_index=0
    for y_index in range(inc_y, len(values), inc_y):
        row=values[y_index]
        # Increment with wraparound
        x_index+=inc_x
        x_index%=len(row)
        if row[x_index]=='#':
            count+=1
    return count

# Part 1
print('Part One: Hit', countTrees(3,1), 'trees')

# Part 2
result = countTrees(1,1)
result*= countTrees(3,1)
result*= countTrees(5,1)
result*= countTrees(7,1)
result*= countTrees(1,2)
print("Part Two:", result, "trees^5")

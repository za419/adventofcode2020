#!/usr/bin/env python3

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()
    
# Trim each line
values=[value.strip() for value in values]

# Part 1
inc_x=3
inc_y=1
count=0
x_index=0
for y_index in range(inc_y, len(values), inc_y):
    row=values[y_index]
    # Increment with wraparound
    x_index+=inc_x
    x_index%=len(row)
    if row[x_index]=='#':
        count+=1
print('Part One: Hit', count, 'trees')

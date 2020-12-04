#!/usr/bin/env python3
import re

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()

# Part 1
# Define how we validate a line
def isValidPart1(line):
    # First, some parsing
    minimum=int(re.match('\d+', line)[0])
    line=line.partition('-')[2]
    maximum=int(re.match('\d+', line)[0])
    character=re.search('[a-zA-Z]', line)[0]
    password=line.partition(': ')[2]

    # Now, count how many times our character appears
    count=0
    for c in password:
        if c==character:
            count+=1
    
    # Return whether the count is in bounds
    return minimum<=count and count<=maximum

# Now map our values into a set of validities
areValid=[isValidPart1(value) for value in values]

# Print out how many values are valid
count=0
for value in areValid:
    if value:
        count+=1
print("Part One: There are", count, "valid entries.")

# Part 2
# Again, define how we validate a line
def isValidPart2(line):
    # First, some parsing
    first=int(re.match('\d+', line)[0])-1
    line=line.partition('-')[2]
    second=int(re.match('\d+', line)[0])-1
    character=re.search('[a-zA-Z]', line)[0]
    password=line.partition(': ')[2]
    
    # Return whether the character is in exactly one of those positions
    return (password[first]==character)!=(password[second]==character)

# And now again...
# Map our values into a set of validities
areValid=[isValidPart2(value) for value in values]

# Print out how many values are valid
count=0
for value in areValid:
    if value:
        count+=1
print("Part Two: There are", count, "valid entries.")

#!/usr/bin/env python3

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()
    
# Trim each line
values=[value.strip() for value in values]

# Assemble groups
groups=[]
group=[]
for value in values:
    if len(value)==0:
        groups.append(group.copy())
        group.clear()
        continue
    group.append(value)
groups.append(group.copy())

group=None
values=None

# Part one: How many times did a group include a character?
def uniqueAnswers(group):
    values=set()
    for line in group:
        values=values.union(set(line))
    return len(values)

count=0
for group in groups:
    count+=uniqueAnswers(group)
print("Part One:", count)

# Part two: How many times did everyone in a group include a character?
def sharedAnswers(group):
    values=set(group[0])
    for line in group:
        values=values.intersection(set(line))
    return len(values)

count=0
for group in groups:
    count+=sharedAnswers(group)
print("Part Two:", count)

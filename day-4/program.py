#!/usr/bin/env python3

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()
    
# Trim each line
values=[value.strip() for value in values]

# Parsing
# Passports will be an array of passports, where each passport is an array of files, where each field is key:value pair
passports=[]
passport=[]
for line in values:
    # If the line is empty, we're ending our passport
    if len(line)==0:
        passports.append(passport)
        passport=[]
        continue
    
    # Parse into field pairs
    fields=line.split(' ')
    fields=[field.partition(':') for field in fields]
    fields=[(field[0], field[2]) for field in fields]

    # Add to passport
    passport+=fields

# If we have a remaining password, add it to the list
if len(passport) != 0:
    passports.append(passport)

# Cleanup
values=None
passport=None

# Part One: Count passports with valid fields.
# First define our validator
def isValid(passport, required=None):
    if required is None:
        # Default to fields required for Part 1
        required=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for requirement in required:
        if True not in (requirement==field[0] for field in passport):
            return False
    return True

# Then count passports that satisfy that condition
count=0
for passport in passports:
    if isValid(passport):
        count+=1

print("Part one:", count, "valid passports.")

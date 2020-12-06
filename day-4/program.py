#!/usr/bin/env python3

import re

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

# Filter down to passwords that are valid for later
validPassports=[passport for passport in passports if isValid(passport)]

print("Part one:", len(validPassports), "valid passports.")

# Part Two: Add validation of field contents.
# First define our validator
def isStrictlyValid(passport):
    # I could make this fancy and generic, but hardcoding is easier.
    # Assume that we don't need to validate which fields a passport includes: We already did!
    for field in passport:
        key, value=field
        if key=='byr':
            # Birth year must be four digits, between 1920 and 2002 inclusive
            try:
                # int() will throw if the year is not entirely digits
                year=int(value)
                # We don't need to check digit counts, 1920>1000
                if year<1920 or year>2002:
                    return False
            except:
                return False
        elif key=='iyr':
            # Issue year must be four digits, between 2010 and 2020 inclusive
            try:
                # int() will throw if the year is not entirely digits
                year=int(value)
                # We don't need to check digit counts, 2010>1000
                if year<2010 or year>2020:
                    return False
            except:
                return False
        elif key=='eyr':
            # Expiration year must be four digits, between 2020 and 2030 inclusive
            try:
                # int() will throw if the year is not entirely digits
                year=int(value)
                # We don't need to check digit counts, 2010>1000
                if year<2020 or year>2030:
                    return False
            except:
                return False
        elif key=='hgt':
            # Height must be a number followed by two characters.
            # The two characters can either be cm or in
            # If cm, then the number must be between 150 and 193 inclusive
            # If in, then the number must be between 59 and 76 inclusive
            # First, split the parts.
            prefix=value[:-2]
            suffix=value[-2:]

            # Is the prefix a number?
            try:
                prefix=int(prefix)
            except:
                return False

            # Now judge based on the suffix
            if suffix=='in':
                if prefix<59 or prefix>76:
                    return False
            elif suffix=='cm':
                if prefix<150 or prefix>193:
                    return False
            else:
                return False
            # Phew! That was long.
        elif key=='hcl':
            # Hair color must be a CSS hex color (#ffffff) with no shortcuts (#fff) or uppercase.
            if not re.match('#[0-9a-f]{6}$', value):
                return False
        elif key=='ecl':
            # Eye color must be one of a set of permitted values
            allowed=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if not value in allowed:
                return False
        elif key=='pid':
            # Password ID must be a nine-digit number
            if not re.match('\d{9}$', value):
                return False
        # We're okay with other fields having whatever values.
    return True

# Count strictly valid passports
count=0
for passport in validPassports:
    if isStrictlyValid(passport):
        count+=1

print("Part Two:", count, "passports have all required fields which fulfill requirements")

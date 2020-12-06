#!/usr/bin/env python3

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()
    
# Trim each line
values=[value.strip() for value in values]

# Part One: Decode some rather insane boarding passes
# Like seriously, what's wrong with '35C'? IT WORKS GOD DAMN YOU
def partition(minimum, maximum, control, low, high):
    i=0
    while minimum<maximum:
        if control[i]==low:
            maximum=minimum+(maximum-minimum)//2
        elif control[i]==high:
            minimum=maximum-(maximum-minimum)//2
        else:
            raise ValueError('Unable to partition')
        i+=1
    return minimum

def calcSeatID(seat):
    # First, do the row
    row=partition(0, 127, seat, 'F', 'B')

    # Now the column
    column=partition(0, 7, seat[7:], 'L', 'R')

    return row*8 + column

# Calculate all IDs
seatIDs=[calcSeatID(seat) for seat in values]
seatIDs.sort(reverse=True)
print("Part One: The largest seat ID is", seatIDs[0])

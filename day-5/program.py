#!/usr/bin/env python3

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()
    
# Trim each line
values=[value.strip() for value in values]

# Part One: Decode some rather insane boarding passes
# Like seriously, what's wrong with '35C'? IT WORKS GOD DAMN YOU
def calcSeatID(seat):
    # First, do the row
    row=0
    minimum=0
    maximum=127
    i=0
    while minimum<maximum:
        if seat[i]=='F':
            maximum=minimum+(maximum-minimum)//2
        elif seat[i]=='B':
            minimum=maximum-(maximum-minimum)//2
        else:
            raise ValueError('Unable to resolve seat number')
        i+=1
    row=minimum

    # Now the column
    column=0
    minimum=0
    maximum=7
    while minimum<maximum:
        print(minimum,maximum,i)
        if seat[i]=='L':
            maximum=minimum+(maximum-minimum)//2
        elif seat[i]=='R':
            minimum=maximum-(maximum-minimum)//2
        else:
            raise ValueError('Unable to resolve seat number')
        i+=1
    column=minimum
    
    return row*8 + column

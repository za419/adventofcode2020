#!/usr/bin/env python3

values=[]

# Read string inputs into values
with open('input', 'r') as file:
    values=file.readlines()

# Convert to integers
values=[int(i) for i in values]

# Now, we could solve this using nested linear searches.
# However, I like writing overcomplicated solutions (unlucky for you), so away we go!

# First, sort values and set our target
values.sort()
target=2020

# Part 1 gets to be a function so it can break cleanly
def part1():
    # Now, we can use binary searches in the inner loop. eevvvilllllll
    for outerIndex in range(len(values)):
        # Notice the insight - Since we're checking in order, we don't need to check values before outerIndex:
        # Those values have already been on the outer side of this check, and we wouldn't be here if they worked
        # with any other numbers
        innerStart=outerIndex+1
        innerEnd=len(values)-1

        # First, lets do some sanity checks.
        # We don't need to bother checking this value if it's so small that its sum with
        # the largest value is <target
        if values[outerIndex]+values[innerEnd]<target:
            continue

        # Similarly, if the value is so large that its sum with the smallest value is >target, fail
        # (This means we don't *really* need to care about the fact that we don't have to have every value be outer)
        if values[outerIndex]+values[0]>target:
            raise ValueError("No such value pair in the input array.")

        while True:
            # Sanity check
            if innerEnd<innerStart:
                break

            # Special case
            if innerEnd==innerStart:
                # If our last value is our result
                if values[outerIndex]+values[innerStart]==target:
                    print("Part one: ", values[outerIndex], "*", values[innerStart], "=", values[outerIndex]*values[innerStart])
                    return
                
                # Otherwise, break
                break

            # Pick an inner index
            innerIndex=innerStart+(innerEnd-innerStart)//2
            
            # Check it.
            # If the sum is equal, we're good.
            if values[outerIndex]+values[innerIndex]==target:
                print("Part one: ", values[outerIndex], "*", values[innerIndex], "=", values[outerIndex]*values[innerIndex])
                return
            
            # If the sum is too small, move innerStart and try again
            elif values[outerIndex]+values[innerIndex]<target:
                innerStart=innerIndex+1

            # And if its too big, move innerEnd and try again
            elif values[outerIndex]+values[innerIndex]>target:
                innerEnd=innerIndex-1
part1()

# Part 2
# This is essentially just part 1 with another loop
for outerIndex in range(len(values)):
    for index in range(len(values)):
        value=values[outerIndex]+values[index]

        # Notice the insight - Since we're checking in order, we don't need to check values before outerIndex:
        # Those values have already been on the outer side of this check, and we wouldn't be here if they worked
        # with any other numbers
        innerStart=index+1
        innerEnd=len(values)-1

        # First, lets do some sanity checks.
        # We don't need to bother checking this value if it's so small that its sum with
        # the largest value is <target
        if value+values[innerEnd]<target:
            continue

        # Similarly, if the value is so large that its sum with the smallest value is >target, fail
        # (This means we don't *really* need to care about the fact that we don't have to have every value be outer)
        if value+values[0]>target:
            raise ValueError("No such value pair in the input array.")

        while True:
            # Sanity check
            if innerEnd<innerStart:
                break

            # Special case
            if innerEnd==innerStart:
                # If our last value is our result
                if value+values[innerStart]==target:
                    print("Part two: ", values[outerIndex], "*", values[index], "*", values[innerStart], "=", values[outerIndex]*values[index]*values[innerStart])
                    exit(0)
                
                # Otherwise, break
                break

            # Pick an inner index
            innerIndex=innerStart+(innerEnd-innerStart)//2
            
            # Check it.
            # If the sum is equal, we're good.
            if value+values[innerIndex]==target:
                print("Part two: ", values[outerIndex], "*", values[index], "*", values[innerIndex], "=", values[outerIndex]*values[index]*values[innerIndex])
                exit(0)
            
            # If the sum is too small, move innerStart and try again
            elif value+values[innerIndex]<target:
                innerStart=innerIndex+1

            # And if its too big, move innerEnd and try again
            elif value+values[innerIndex]>target:
                innerEnd=innerIndex-1

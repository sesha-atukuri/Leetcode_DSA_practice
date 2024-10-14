"""Array Sum:
Write a function that takes an array of integers and returns the sum of all the integers in the array.

Example:

makefile
Copy code
Input: [3, 6, 1, 8, 2]
Output: 20"""

def sumarray(inlist):
    sum = 0
    for i in inlist:
        sum += i
    print(sum)


sumarray([3,6,1,8,2])
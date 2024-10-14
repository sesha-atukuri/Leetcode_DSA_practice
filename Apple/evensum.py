"""Write a function that takes an array of numbers as input and returns
 the sum of all even numbers in the array.

Example:
Input: [2, 5, 8, 10, 15]
Output: 20 (2 + 8 + 10)"""

def numsum(inlist):
    target = 0
    for i in inlist:
        if i%2 == 0:
            target += i
    print(target)


numsum([2,5,8,10,15])


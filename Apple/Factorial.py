"""Factorial Calculation:
Write a function to calculate the factorial of a positive integer n. The factorial of n is the product of all positive integers from 1 to n.

Example:

makefile
Copy code
Input: 5
Output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)"""

def recurse(num):
    i, output = 1, 1
    while i <= num:
        output *= i
        i += 1
    print(output)


recurse(5)
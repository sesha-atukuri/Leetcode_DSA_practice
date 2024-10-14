"""Fibonacci Sequence:
Write a function that generates the first n numbers in the Fibonacci sequence.

Example:

makefile
Copy code
Input: 7
Output: [0, 1, 1, 2, 3, 5, 8]"""


def fib(inputnum):
    i = 2
    output = [0,1]
    print(inputnum)
    while i < inputnum:
        sum = output[i-1] + output[i - 2]
        output.append(sum)
        i=i+1
    print(output,"final")


fib(7)

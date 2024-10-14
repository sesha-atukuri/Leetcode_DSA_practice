'''Write a function that takes a string as input and returns true if the string is a palindrome
(reads the same forwards and backwards), and false otherwise.

Example:
Input: "racecar"
Output: true'''


def palli(instr):
    outstr = ''
    for idx in range(len(instr)):
        outstr += instr[len(instr) - 1 - idx]
    if instr == outstr:
        print('pallindrome')
    else:
        print('not pallindrome')


palli('malayalam')

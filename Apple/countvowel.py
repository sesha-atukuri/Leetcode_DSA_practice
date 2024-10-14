"""Question: Count Vowels

Write a function that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string.

Example:
Input: "Hello, World!"
Output: 3"""

def countvow(instr):
    count = 0
    vow =['a','e','i','o','u']
    for i in range(len(instr)):
        if instr[i] in vow:
            count += 1
    print(count)

countvow("Helloei, World!")
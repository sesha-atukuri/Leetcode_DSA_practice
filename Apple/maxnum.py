"""Question: Find the Maximum Element

Write a function that takes a list of integers as input and returns the maximum element in the list.

Example:
Input: [4, 7, 2, 9, 1]
Output: 9"""


def maxel(numli):
    maxnum = 0
    for i in numli:
        if maxnum < i:
            maxnum = i

    print(maxnum)


maxel([4, 709, 2, 9, 10,98])
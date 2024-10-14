"""Duplicate Removal:
Write a function that takes an array of integers and removes any duplicates, returning a new array without duplicates.

Example:

makefile
Copy code
Input: [2, 3, 3, 6, 2, 8]
Output: [2, 3, 6, 8]"""


def remov(inlist):
    ouli = []
    for i in inlist:
        if i not in ouli:
            ouli.append(i)
    print(ouli)


remov([2, 3, 3, 6, 2, 8])
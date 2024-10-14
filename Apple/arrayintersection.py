"""Array Intersection:
Write a function that takes two arrays as input and returns an array containing elements that are present in both arrays.

Example:

makefile
Copy code
Input: [2, 4, 6, 8], [4, 8, 10]
Output: [4, 8]"""


def intersection(ar1, ar2):
    outar = []
    for i in ar1:
        if i in ar2:
            outar.append(i)
    print(outar)

intersection([2, 4, 6, 8], [4, 8, 2, 10])
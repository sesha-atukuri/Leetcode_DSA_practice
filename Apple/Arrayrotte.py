"""Array Rotation:
Write a function that rotates the elements of an array to the right by a specified number of positions.

Example:

makefile
Copy code
Input: [1, 2, 3, 4, 5], 2
Output: [4, 5, 1, 2, 3]"""


def rotate(inar, pos):
    ouar = [0,0,0,0,0,0]
    s =0
    for i in range(len(inar)):

        if (i + pos) > len(inar)-1:
            ouar[(i+pos)-len(inar)] = inar[i]

        else:
            ouar[i+pos] = inar[i]


    print(ouar)


rotate([1, 2, 3, 4, 5,6], 3)

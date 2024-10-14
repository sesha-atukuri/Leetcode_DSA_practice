#Tower of Hanoi is a mathematical puzzle where we have three pegs and n disks.
# The objective of the puzzle is to move the entire stack to another peg, obeying the following simple rules:

#Only one disk can be moved at a time.
#Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
#No disk may be placed on top of a smaller disk.
#Given n denoting the number of disks in the first peg, return all the steps required to move all disks from the first peg to the third peg in minimal number of steps.

def tower_of_hanoi(n):

    result = helper(n,1,2,3)
    return result

def helper(n,s,aux,d):
    result = {}
    if n == 1:
        return result(s, d)
    helper(n-1,s,d,aux)
    result.append(s,d)
    helper(n-1,aux,s,d)

    return result


print(tower_of_hanoi(4))
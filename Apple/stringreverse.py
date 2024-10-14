'''Question: String Reversal

Write a function that takes a string as input and returns the reverse of that string.

Example:
Input: "hello"
Output: "olleh"'''


def strrevese(strs):
    outstr = ''

    for idx in range(len(strs)):
        outstr += strs[len(strs)-1-idx]
    print(outstr)


strrevese('hello')

"""String Anagram Check:
Write a function that takes two strings as input and returns true
if they are anagrams (contain the same characters in any order), and false otherwise.

Example:

vbnet
Copy code
Input: "listen", "silent"
Output: true"""


def strana(str1, str2):
    d1, d2 = {}, {}

    for i in range(len(str1)):
        if str1[i] in d1:
            d1[str1[i]] += i
        else:
            d1[str1[i]] = 1

    for j in range(len(str2)):
        if str2[j] in d2:
            d2[str2[j]] += j
        else:
            d2[str2[j]] = 1

    if d1 == d2:
        print('true')
    else:
        print('false')


strana("listeny", "silent")

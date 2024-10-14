"""Write a function that takes an integer as input and returns true if it's a prime number (divisible only by 1 and itself), and false otherwise.

Example:

vbnet
Copy code
Input: 7
Output: true"""


def primenum(num):
    i, count = 2, 0
    while i <= 7:
        if num % i != 0:
            count += 1
        i += 1
    if count == 4:
        print("prime")


primenum()
